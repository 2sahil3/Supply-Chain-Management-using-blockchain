from datetime import datetime
import json
from web3 import Web3
from datetime import datetime
from hexbytes import HexBytes
from abi import ABI
from web3.middleware import geth_poa_middleware
import time

ganach_url = "http://127.0.0.1:7546"
web3 = Web3(Web3.HTTPProvider(ganach_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
#web3 = Web3(Web3.EthereumTesterProvider)
web3.eth.defaultAccount = web3.eth.accounts[0]
#address = web3.toChecksumAddress("0xd9145CCE52D386f254917e481eB44e9943F39138")
contract = web3.eth.contract(
    address="0xFD9F9d320819ECEd465c6C1497Bfa5d564136b6D", abi=ABI)
# contract = web3.eth.contract(abi = abi, bytecode = bytecode )
# print(web3.eth.get_block('latest'))

# print(msg_hash)
# print(type(msg_hash))

# web3.utils.padLeft(web3.utils.hexToBytes(msg_hash), 32)
# msg_hashbytes = HexBytes(msg_hash)
# print(msg_hash.hex())


signer_account = web3.eth.accounts[0]
# signer_private = '0x1f03802300a542709b103fc04b631f20e5ae72792b4aa96a9990b4ee39d09d74'
nonce = web3.eth.get_transaction_count(signer_account)
timeStamp = str(time.time())

print(nonce)
# tx = {
#     'nonce': nonce+1,
#     'to': web3.eth.accounts[1],
#     'value': web3.toWei(1, 'ether'),
#     'gas': 2000000,
#     'gasPrice': web3.toWei('50', 'gwei')
# }
# msg_hash = contract.functions.getMessageHash(web3.eth.accounts[1],web3.toWei(1,'ether'),"first transaction",nonce).transact()

# get transaction hash
# print(web3.toHex(tx_hash))


# verifyer_acc = web3.eth.accounts[1]
# print(web3.eth.accounts[0].verify(signed_tx, msg_hash))


def settime():
    now = "prateek"
#  print(now)
    tx_hash = contract.functions.setTimeStamp(now).transact()
    return tx_hash


def gettime():
    time = contract.functions.getTimeStamp().call()
    return time


def create_product(
    timeStamp, itemName, mfgDate, expiryDate, batchNo, numberUnits
):

    tx = contract.functions.createProduct(
        itemName,
        timeStamp,
        mfgDate,
        expiryDate,
        batchNo,
        numberUnits
    ).buildTransaction({'from': signer_account})

    signed_tx = web3.eth.account.sign_Transaction(
        tx, '0x68e6a2d8315b68a792e06b8995e2d6846cdb67c6b7781445e6d341d63d408fd6')
    hash_txn = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(hash_txn)


create_product(
    timeStamp=timeStamp,
    itemName="item",
    mfgDate=timeStamp,
    expiryDate=timeStamp,
    batchNo="256",
    numberUnits=123
)


def last():
    return contract.functions.getLastIndex().call()


def get_product(productId):
    productData = contract.functions.getProductDetails(productId).call()
    return productData


# hash = settime()
# time = gettime()
# tx_receipt = web3.eth.wait_for_transaction_receipt(hash)
# print(tx_receipt.contractAddress)
# time = gettime()
# print(hash)
# print(time)
