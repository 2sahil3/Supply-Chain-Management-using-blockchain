ABI = '''[
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "item_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "time_stamp",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "mfg_date",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "expiry_date",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "batch_no",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "numOfItem",
				"type": "uint256"
			}
		],
		"name": "createProduct",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getLastIndex",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "timestamp",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "itemName",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "mfgDate",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "expiryDate",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "batchNo",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "numberOfItem",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "productId",
						"type": "uint256"
					}
				],
				"internalType": "struct Contract_supplychain.Product",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "item_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "time_stamp",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "mfg_date",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "expiry_date",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "batch_no",
				"type": "string"
			}
		],
		"name": "createHash",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "_messageHash",
				"type": "bytes32"
			}
		],
		"name": "getEthSignedMessageHash",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "productId",
				"type": "uint256"
			}
		],
		"name": "getProductDetails",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "timestamp",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "itemName",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "mfgDate",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "expiryDate",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "batchNo",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "numberOfItem",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "productId",
						"type": "uint256"
					}
				],
				"internalType": "struct Contract_supplychain.Product",
				"name": "",
				"type": "tuple"
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
		"name": "products",
		"outputs": [
			{
				"internalType": "string",
				"name": "timestamp",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "itemName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "mfgDate",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "expiryDate",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "batchNo",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "numberOfItem",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "productId",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "runningProductId",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]'''
