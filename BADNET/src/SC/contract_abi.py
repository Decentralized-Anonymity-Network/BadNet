abi = [
	{
		"inputs": [
			{
				"internalType": "address payable",
				"name": "addr",
				"type": "address"
			}
		],
		"name": "contract_transfer_to_relay",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint16",
				"name": "size",
				"type": "uint16"
			},
			{
				"internalType": "uint16[]",
				"name": "list",
				"type": "uint16[]"
			}
		],
		"name": "modifyHealthFlag",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "relay_cancellation",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "relay_register",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint8",
				"name": "_counter",
				"type": "uint8"
			},
			{
				"internalType": "bytes",
				"name": "_Hdr",
				"type": "bytes"
			},
			{
				"internalType": "bytes",
				"name": "_encryptedSRI",
				"type": "bytes"
			},
			{
				"internalType": "bytes",
				"name": "_NSD",
				"type": "bytes"
			}
		],
		"name": "relay_upload_SRI_and_NSD",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "period",
				"type": "uint256"
			}
		],
		"name": "setSRIperiod",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"stateMutability": "payable",
		"type": "fallback"
	},
	{
		"stateMutability": "payable",
		"type": "receive"
	},
	{
		"inputs": [],
		"name": "client_download_NSD",
		"outputs": [
			{
				"internalType": "bool[]",
				"name": "",
				"type": "bool[]"
			},
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint16",
				"name": "i",
				"type": "uint16"
			}
		],
		"name": "getHealthFlag",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint16",
				"name": "i",
				"type": "uint16"
			}
		],
		"name": "getinfo",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			},
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			},
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			},
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getrelayIndex",
		"outputs": [
			{
				"internalType": "uint16",
				"name": "",
				"type": "uint16"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint16",
				"name": "i",
				"type": "uint16"
			}
		],
		"name": "relay_download_SRI",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			},
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			},
			{
				"internalType": "bytes",
				"name": "",
				"type": "bytes"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint8",
				"name": "counter",
				"type": "uint8"
			}
		],
		"name": "relay_get_counter_list",
		"outputs": [
			{
				"internalType": "bool[]",
				"name": "",
				"type": "bool[]"
			},
			{
				"internalType": "uint16[][]",
				"name": "",
				"type": "uint16[][]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "relay_get_current_counter",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "relay_get_index_set",
		"outputs": [
			{
				"internalType": "uint16",
				"name": "",
				"type": "uint16"
			},
			{
				"internalType": "uint16[]",
				"name": "",
				"type": "uint16[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "relay_get_upload_period",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "relay_registration_check",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "unhealthyRelaySet",
		"outputs": [
			{
				"internalType": "uint16",
				"name": "",
				"type": "uint16"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
