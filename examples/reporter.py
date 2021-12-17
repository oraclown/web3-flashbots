"""
Minimal viable example of flashbots usage with dynamic fee transactions.
"""

import os

from eth_account.account import Account
from eth_account.signers.local import LocalAccount
from flashbots import flashbot
from web3 import Web3, HTTPProvider
from web3.exceptions import TransactionNotFound
from web3.types import TxParams
from dotenv import load_dotenv, find_dotenv

from telliot_core.apps.telliot_config import TelliotConfig
from telliot_core.contract.contract import Contract
from telliot_core.queries.legacy_query import LegacyRequest
from examples.abi import gorli_playground_abi
# from telliot_feed_examples.utils.log import get_logger


load_dotenv(find_dotenv())
# logger = get_logger(__name__)


def env(key: str) -> str:
    return os.environ.get(key)


def main() -> None:
    # account to send the transfer and sign transactions
    account: LocalAccount = Account.from_key(env("SENDER_PRIVATE_KEY"))
    # account to establish flashbots reputation
    # NOTE: it should not store funds
    signature: LocalAccount = Account.from_key(env("SIGNATURE_PRIVATE_KEY"))
    chain_id = 5

    w3 = Web3(HTTPProvider(env("PROVIDER")))
    flashbot(w3, signature, env("FLASHBOTS_HTTP_PROVIDER_URI"))

    print(f"Reporter account balance: {Web3.fromWei(w3.eth.get_balance(account.address), 'ether')} ETH")

    playground = w3.eth.contract(
        address="0x3477EB82263dabb59AC0CAcE47a61292f28A2eA7",  # Gorli playground addr
        abi=gorli_playground_abi)
    
    query = LegacyRequest(legacy_id=99)
    nonce_getter = playground.get_function_by_name("getNewValueCountbyQueryId")
    timestamp_count = nonce_getter(_queryId=query.query_id).call()
    print('timestamp count (nonce):', timestamp_count)

    submit_val_func = playground.get_function_by_name("submitValue")
    submit_val_tx = submit_val_func(
        _queryId=query.query_id,
        _value=query.value_type.encode(420.0),
        _nonce=timestamp_count,
        _queryData=query.query_data,
    )

    acc_nonce = w3.eth.get_transaction_count(account.address)
    built_submit_val_tx = submit_val_tx.buildTransaction(
        {
            "nonce": acc_nonce,
            "gas": 350000,
            "maxFeePerGas": Web3.toWei(200, "gwei"),
            "maxPriorityFeePerGas": Web3.toWei(50, "gwei"),
            "chainId": chain_id,
        }
    )
    submit_val_tx_signed = account.sign_transaction(built_submit_val_tx)

    # return

    # bundle two EIP-1559 (type 2) transactions, pre-sign one of them
    # NOTE: chainId is necessary for all EIP-1559 txns
    # NOTE: nonce is required for signed txns

    # nonce = w3.eth.get_transaction_count(account.address)
    # tx1: TxParams = {
    #     "to": receiver.address,
    #     "value": Web3.toWei(0.01, "ether"),
    #     "gas": 25000,
    #     "maxFeePerGas": Web3.toWei(200, "gwei"),
    #     "maxPriorityFeePerGas": Web3.toWei(50, "gwei"),
    #     "nonce": nonce,
    #     "chainId": chain_id,
    # }
    # tx1_signed = account.sign_transaction(tx1)

    # tx2: TxParams = {
    #     "to": receiver.address,
    #     "value": Web3.toWei(0.01, "ether"),
    #     "gas": 25000,
    #     "maxFeePerGas": Web3.toWei(200, "gwei"),
    #     "maxPriorityFeePerGas": Web3.toWei(50, "gwei"),
    #     "chainId": chain_id,
    # }

    bundle = [
        {"signed_transaction": submit_val_tx_signed.rawTransaction},
        # {"signed_transaction": tx1_signed.rawTransaction},
        # {"signer": sender, "transaction": tx2},
    ]

    # send bundle to be executed in the next 5 blocks
    block = w3.eth.block_number
    results = []
    for target_block in [block + k for k in [1, 2, 3, 4, 5]]:
        results.append(w3.flashbots.send_bundle(bundle, target_block_number=target_block))
    print(f"Bundle sent to miners in block {block}")

    # wait for the results
    results[-1].wait()
    try:
        receipt = results[-1].receipts()
        print(f"Bundle was executed in block {receipt[0].blockNumber}")
    except TransactionNotFound:
        print("Bundle was not executed")
        return
    
    print(f"Sender account balance: {Web3.fromWei(w3.eth.get_balance(account.address), 'ether')} ETH")


if __name__ == "__main__":
    main()
