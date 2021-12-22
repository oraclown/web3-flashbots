"""ABIs for contracts."""

gorli_playground_abi = [
    {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "spender",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "Approval",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "bytes32",
                "name": "_queryId",
                "type": "bytes32",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_time",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "bytes",
                "name": "_value",
                "type": "bytes",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_reward",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_nonce",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "bytes",
                "name": "_queryData",
                "type": "bytes",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "_reporter",
                "type": "address",
            },
        ],
        "name": "NewReport",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "_user",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "bytes32",
                "name": "_queryId",
                "type": "bytes32",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_tip",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "_totalTip",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "bytes",
                "name": "_queryData",
                "type": "bytes",
            },
        ],
        "name": "TipAdded",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
            },
        ],
        "name": "Transfer",
        "type": "event",
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "name": "addresses",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_owner", "type": "address"},
            {"internalType": "address", "name": "_spender", "type": "address"},
        ],
        "name": "allowance",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_spender", "type": "address"},
            {"internalType": "uint256", "name": "_amount", "type": "uint256"},
        ],
        "name": "approve",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_account", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "_queryId", "type": "bytes32"},
            {"internalType": "uint256", "name": "_timestamp", "type": "uint256"},
        ],
        "name": "beginDispute",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "decimals",
        "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_user", "type": "address"}],
        "name": "faucet",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "_queryId", "type": "bytes32"}],
        "name": "getCurrentReward",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "_queryId", "type": "bytes32"}],
        "name": "getNewValueCountbyQueryId",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "_queryId", "type": "bytes32"},
            {"internalType": "uint256", "name": "_index", "type": "uint256"},
        ],
        "name": "getTimestampbyQueryIdandIndex",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "_hash", "type": "bytes32"}],
        "name": "getVoteRounds",
        "outputs": [{"internalType": "uint256[]", "name": "", "type": "uint256[]"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
        ],
        "name": "isDisputed",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "_queryId", "type": "bytes32"},
            {"internalType": "uint256", "name": "_timestamp", "type": "uint256"},
        ],
        "name": "retrieveData",
        "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "_queryId", "type": "bytes32"},
            {"internalType": "bytes", "name": "_value", "type": "bytes"},
            {"internalType": "uint256", "name": "_nonce", "type": "uint256"},
            {"internalType": "bytes", "name": "_queryData", "type": "bytes"},
        ],
        "name": "submitValue",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "timeBasedReward",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "timeOfLastNewValue",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
        ],
        "name": "timestamps",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "_queryId", "type": "bytes32"},
            {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            {"internalType": "bytes", "name": "_queryData", "type": "bytes"},
        ],
        "name": "tipQuery",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "name": "tips",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "tipsInContract",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_recipient", "type": "address"},
            {"internalType": "uint256", "name": "_amount", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_sender", "type": "address"},
            {"internalType": "address", "name": "_recipient", "type": "address"},
            {"internalType": "uint256", "name": "_amount", "type": "uint256"},
        ],
        "name": "transferFrom",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
        ],
        "name": "values",
        "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "voteCount",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
        ],
        "name": "voteRounds",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
]

mainnet_oracle_abi = [
    {
        "anonymous":False,
        "inputs":[
            {
                "indexed":False,
                "internalType":"bytes32",
                "name":"_queryId",
                "type":"bytes32"
            },
            {
                "indexed":False,
                "internalType":"uint256",
                "name":"_time",
                "type":"uint256"
            },
            {
                "indexed":False,
                "internalType":"bytes",
                "name":"_value",
                "type":"bytes"
            },
            {
                "indexed":False,
                "internalType":"uint256",
                "name":"_reward",
                "type":"uint256"
            },
            {
                "indexed":False,
                "internalType":"uint256",
                "name":"_nonce",
                "type":"uint256"
            },
            {
                "indexed":False,
                "internalType":"bytes",
                "name":"_queryData",
                "type":"bytes"
            },
            {
                "indexed":False,
                "internalType":"address",
                "name":"_reporter",
                "type":"address"
            }
        ],
        "name":"NewReport",
        "type":"event"
    },
    {
        "anonymous":False,
        "inputs":[
            {
                "indexed":False,
                "internalType":"uint256",
                "name":"_newReportingLock",
                "type":"uint256"
            }
        ],
        "name":"ReportingLockChanged",
        "type":"event"
    },
    {
        "anonymous":False,
        "inputs":[
            {
                "indexed":False,
                "internalType":"uint256",
                "name":"_newTimeBasedReward",
                "type":"uint256"
            }
        ],
        "name":"TimeBasedRewardsChanged",
        "type":"event"
    },
    {
        "anonymous":False,
        "inputs":[
            {
                "indexed":True,
                "internalType":"address",
                "name":"_user",
                "type":"address"
            },
            {
                "indexed":True,
                "internalType":"bytes32",
                "name":"_queryId",
                "type":"bytes32"
            },
            {
                "indexed":False,
                "internalType":"uint256",
                "name":"_tip",
                "type":"uint256"
            },
            {
                "indexed":False,
                "internalType":"uint256",
                "name":"_totalTip",
                "type":"uint256"
            },
            {
                "indexed":False,
                "internalType":"bytes",
                "name":"_queryData",
                "type":"bytes"
            }
        ],
        "name":"TipAdded",
        "type":"event"
    },
    {
        "inputs":[
            {
                "internalType":"uint256",
                "name":"_newReportingLock",
                "type":"uint256"
            }
        ],
        "name":"changeReportingLock",
        "outputs":[
            
        ],
        "stateMutability":"nonpayable",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"uint256",
                "name":"_newTimeBasedReward",
                "type":"uint256"
            }
        ],
        "name":"changeTimeBasedReward",
        "outputs":[
            
        ],
        "stateMutability":"nonpayable",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"_queryId",
                "type":"bytes32"
            },
            {
                "internalType":"uint256",
                "name":"_timestamp",
                "type":"uint256"
            }
        ],
        "name":"getBlockNumberByTimestamp",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"_queryId",
                "type":"bytes32"
            }
        ],
        "name":"getCurrentReward",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            },
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"_queryId",
                "type":"bytes32"
            }
        ],
        "name":"getCurrentValue",
        "outputs":[
            {
                "internalType":"bytes",
                "name":"",
                "type":"bytes"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"_queryId",
                "type":"bytes32"
            },
            {
                "internalType":"uint256",
                "name":"_index",
                "type":"uint256"
            }
        ],
        "name":"getReportTimestampByIndex",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"_queryId",
                "type":"bytes32"
            },
            {
                "internalType":"uint256",
                "name":"_timestamp",
                "type":"uint256"
            }
        ],
        "name":"getReporterByTimestamp",
        "outputs":[
            {
                "internalType":"address",
                "name":"",
                "type":"address"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"address",
                "name":"_reporter",
                "type":"address"
            }
        ],
        "name":"getReporterLastTimestamp",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            
        ],
        "name":"getReportingLock",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"address",
                "name":"_reporter",
                "type":"address"
            }
        ],
        "name":"getReportsSubmittedByAddress",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            
        ],
        "name":"getTimeBasedReward",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            
        ],
        "name":"getTimeOfLastNewValue",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"_queryId",
                "type":"bytes32"
            }
        ],
        "name":"getTimestampCountById",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"_queryId",
                "type":"bytes32"
            },
            {
                "internalType":"uint256",
                "name":"_timestamp",
                "type":"uint256"
            }
        ],
        "name":"getTimestampIndexByTimestamp",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"_queryId",
                "type":"bytes32"
            }
        ],
        "name":"getTipsById",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"address",
                "name":"_user",
                "type":"address"
            }
        ],
        "name":"getTipsByUser",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"_queryId",
                "type":"bytes32"
            },
            {
                "internalType":"uint256",
                "name":"_timestamp",
                "type":"uint256"
            }
        ],
        "name":"getValueByTimestamp",
        "outputs":[
            {
                "internalType":"bytes",
                "name":"",
                "type":"bytes"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"_queryId",
                "type":"bytes32"
            },
            {
                "internalType":"uint256",
                "name":"_timestamp",
                "type":"uint256"
            }
        ],
        "name":"removeValue",
        "outputs":[
            
        ],
        "stateMutability":"nonpayable",
        "type":"function"
    },
    {
        "inputs":[
            
        ],
        "name":"reportingLock",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"_queryId",
                "type":"bytes32"
            },
            {
                "internalType":"bytes",
                "name":"_value",
                "type":"bytes"
            },
            {
                "internalType":"uint256",
                "name":"_nonce",
                "type":"uint256"
            },
            {
                "internalType":"bytes",
                "name":"_queryData",
                "type":"bytes"
            }
        ],
        "name":"submitValue",
        "outputs":[
            
        ],
        "stateMutability":"nonpayable",
        "type":"function"
    },
    {
        "inputs":[
            
        ],
        "name":"timeBasedReward",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            
        ],
        "name":"timeOfLastNewValue",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"_queryId",
                "type":"bytes32"
            },
            {
                "internalType":"uint256",
                "name":"_tip",
                "type":"uint256"
            },
            {
                "internalType":"bytes",
                "name":"_queryData",
                "type":"bytes"
            }
        ],
        "name":"tipQuery",
        "outputs":[
            
        ],
        "stateMutability":"nonpayable",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"",
                "type":"bytes32"
            }
        ],
        "name":"tips",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            
        ],
        "name":"tipsInContract",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            
        ],
        "name":"verify",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"pure",
        "type":"function"
    }
]


mainnet_master_abi = [
    {
        "inputs":[
            {
                "internalType":"address",
                "name":"_tContract",
                "type":"address"
            },
            {
                "internalType":"address",
                "name":"_oTellor",
                "type":"address"
            }
        ],
        "stateMutability":"nonpayable",
        "type":"constructor"
    },
    {
        "anonymous":False,
        "inputs":[
            {
                "indexed":False,
                "internalType":"address",
                "name":"_newTellor",
                "type":"address"
            }
        ],
        "name":"NewTellorAddress",
        "type":"event"
    },
    {
        "stateMutability":"payable",
        "type":"fallback"
    },
    {
        "inputs":[
            {
                "internalType":"address",
                "name":"",
                "type":"address"
            },
            {
                "internalType":"address",
                "name":"",
                "type":"address"
            }
        ],
        "name":"_allowances",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"",
                "type":"bytes32"
            }
        ],
        "name":"addresses",
        "outputs":[
            {
                "internalType":"address",
                "name":"",
                "type":"address"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"address",
                "name":"",
                "type":"address"
            },
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "name":"balances",
        "outputs":[
            {
                "internalType":"uint128",
                "name":"fromBlock",
                "type":"uint128"
            },
            {
                "internalType":"uint128",
                "name":"value",
                "type":"uint128"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"",
                "type":"bytes32"
            }
        ],
        "name":"bytesVars",
        "outputs":[
            {
                "internalType":"bytes32",
                "name":"",
                "type":"bytes32"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"address",
                "name":"_newDeity",
                "type":"address"
            }
        ],
        "name":"changeDeity",
        "outputs":[
            
        ],
        "stateMutability":"nonpayable",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"address",
                "name":"_newOwner",
                "type":"address"
            }
        ],
        "name":"changeOwner",
        "outputs":[
            
        ],
        "stateMutability":"nonpayable",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"address",
                "name":"_tContract",
                "type":"address"
            }
        ],
        "name":"changeTellorContract",
        "outputs":[
            
        ],
        "stateMutability":"nonpayable",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "name":"currentMiners",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"value",
                "type":"uint256"
            },
            {
                "internalType":"address",
                "name":"miner",
                "type":"address"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"",
                "type":"bytes32"
            }
        ],
        "name":"disputeIdByDisputeHash",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "name":"disputesById",
        "outputs":[
            {
                "internalType":"bytes32",
                "name":"hash",
                "type":"bytes32"
            },
            {
                "internalType":"int256",
                "name":"tally",
                "type":"int256"
            },
            {
                "internalType":"bool",
                "name":"executed",
                "type":"bool"
            },
            {
                "internalType":"bool",
                "name":"disputeVotePassed",
                "type":"bool"
            },
            {
                "internalType":"bool",
                "name":"isPropFork",
                "type":"bool"
            },
            {
                "internalType":"address",
                "name":"reportedMiner",
                "type":"address"
            },
            {
                "internalType":"address",
                "name":"reportingParty",
                "type":"address"
            },
            {
                "internalType":"address",
                "name":"proposedForkAddress",
                "type":"address"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"address",
                "name":"",
                "type":"address"
            }
        ],
        "name":"migrated",
        "outputs":[
            {
                "internalType":"bool",
                "name":"",
                "type":"bool"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"",
                "type":"bytes32"
            },
            {
                "internalType":"address",
                "name":"",
                "type":"address"
            }
        ],
        "name":"minersByChallenge",
        "outputs":[
            {
                "internalType":"bool",
                "name":"",
                "type":"bool"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "name":"newValueTimestamps",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"",
                "type":"bytes32"
            }
        ],
        "name":"requestIdByQueryHash",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    },
    {
        "inputs":[
            {
                "internalType":"bytes32",
                "name":"",
                "type":"bytes32"
            }
        ],
        "name":"uints",
        "outputs":[
            {
                "internalType":"uint256",
                "name":"",
                "type":"uint256"
            }
        ],
        "stateMutability":"view",
        "type":"function"
    }
]
