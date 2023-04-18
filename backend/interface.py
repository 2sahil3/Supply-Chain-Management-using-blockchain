from web3 import Web3
from abi import ABI
import time
global web3, signer_account, contract


def interfaceInit():
    ganach_url = "http://127.0.0.1:7546"
    global web3
    web3 = Web3(Web3.HTTPProvider(ganach_url))
    web3.eth.defaultAccount = web3.eth.accounts[0]
    global contract
    contract = web3.eth.contract(
        address="0x2A3A989d608Ec2422B40143dC809dd7faFDF752f", abi=ABI)
    global signer_account
    signer_account = web3.eth.accounts[0]


def selectAccount(number):
    global signer_account
    signer_account = web3.eth.accounts[number]


timeStamp = str(time.time())


def create_product(timeStamp, itemName, mfgDate, expiryDate, batchNo, numberUnits, history, par, user_address):
    global web3
    nonce = web3.eth.get_transaction_count(user_address)

    addr = web3.to_hex(bytes(user_address, 'utf-8'))
    tx = contract.functions.createProduct(
        itemName,
        mfgDate,
        expiryDate,
        batchNo,
        numberUnits,
        history,
        par,
        user_address
    ).build_transaction({'from': user_address, 'nonce': nonce})

    # print("tx: " + str(tx))

    signed_tx = web3.eth.account.sign_transaction(
        tx, '0x17a64878f44eb58c63947e1c7f3ca6ecc46c722fba2524ec93100ae14a1944c1')
    hash_txn = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    # print("tx_hash: "+str(hash_txn))


# def addState(product_id, time_stamp, loc):
#     nonce = web3.eth.get_transaction_count(signer_account)
#     tx = contract.functions.addState(product_id,time_stamp,loc).buildTransaction({'from': signer_account, 'nonce': nonce})
#     signed_tx = web3.eth.account.signTransaction(tx, '0x6727e3c0a0187676c78ff449e9ce460ae1b3479b10e71e59a94414865c8033bc')
#     hash_txn = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

def getStates(product_id):
    states = contract.functions.getState(product_id).call()

# def lastGlobalProductId():
#     return contract.functions.getLastIndex().call() -1


def getAllProducts(pid):
    return contract.functions.findProduct(pid).call()


def get_product(productId):
    productData = contract.functions.getProductDetails(productId).call()
    return productData


def getLastProductID(address):
    id = contract.functions.getLastProductId(address).call()
    return id


interfaceInit()
# create_product()
