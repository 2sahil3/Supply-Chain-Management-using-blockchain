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
			},
			{
				"internalType": "string",
				"name": "history",
				"type": "string"
			},
			{
				"internalType": "int256",
				"name": "parent",
				"type": "int256"
			},
			{
				"internalType": "address",
				"name": "user_address",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to_Address",
				"type": "address"
			}
		],
		"name": "createProduct",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "person",
				"type": "address"
			}
		],
		"name": "findProduct",
		"outputs": [
			{
				"components": [
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
						"internalType": "string",
						"name": "current_history",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "ID",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "numberOfItem",
						"type": "uint256"
					}
				],
				"internalType": "struct Contract_supplychain.Product[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getLastIndex",
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
		"inputs": [
			{
				"internalType": "address",
				"name": "addr",
				"type": "address"
			}
		],
		"name": "getLastProductId",
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
						"internalType": "string",
						"name": "current_history",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "ID",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "numberOfItem",
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
				"internalType": "string",
				"name": "current_history",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "ID",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "numberOfItem",
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
