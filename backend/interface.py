from web3 import Web3
from abi import ABI
import time

global web3, signer_account, contract

def interfaceInit():
    ganach_url = "http://127.0.0.1:7545"
    web3 = Web3(Web3.HTTPProvider(ganach_url))
    web3.eth.defaultAccount = web3.eth.accounts[0]
    global contract
    contract = web3.eth.contract(
        address="0x5639A5937260Fc660c067DEa48F4869DF8FaDCB8", abi=ABI)
    global signer_account
    signer_account = web3.eth.accounts[0]

# print(signer_account)

def selectAccount(number):
    global signer_account
    signer_account = web3.eth.accounts[number]

timeStamp = str(time.time())


def create_product(timeStamp, itemName, mfgDate, expiryDate, batchNo, numberUnits,history,par,user_address):
    nonce = web3.eth.get_transaction_count(signer_account)
    addr = web3.toHex(bytes(user_address, 'utf-8'))
    tx = contract.functions.createProduct(
        itemName,
        mfgDate,
        expiryDate,
        batchNo,
        numberUnits,
        history,
        par,
        user_address
    ).buildTransaction({'from': signer_account, 'nonce': nonce})

    signed_tx = web3.eth.account.signTransaction(
        tx, '0x6727e3c0a0187676c78ff449e9ce460ae1b3479b10e71e59a94414865c8033bc')
    hash_txn = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

def addState(product_id, time_stamp, loc):
    nonce = web3.eth.get_transaction_count(signer_account)
    tx = contract.functions.addState(product_id,time_stamp,loc).buildTransaction({'from': signer_account, 'nonce': nonce})
    signed_tx = web3.eth.account.signTransaction(tx, '0x6727e3c0a0187676c78ff449e9ce460ae1b3479b10e71e59a94414865c8033bc')
    hash_txn = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

def getStates(product_id):
    states = contract.functions.getState(product_id).call()

def lastProductId():
    return contract.functions.getLastIndex().call() -1

def getAllProducts():
    return contract.functions.findProduct(signer_account).call()

def get_product(productId):
    productData = contract.functions.getProductDetails(productId).call()
    return productData



interfaceInit()

lastProductId()

