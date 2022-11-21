from web3 import Web3, HTTPProvider
import contract_abi
import account

import os
import time
import binascii
import hashlib
import zlib
import re
from Crypto.Cipher import AES
import secrets
from ecies import encrypt

web3 = Web3(HTTPProvider("https://goerli.infura.io/v3/67631e6ab6fc44e49915da74fd957740"))
contract_instance = web3.eth.contract(address=account.contract_address, abi=contract_abi.abi)
AES_CBC_IV = b'qqqqqqqqqqqqqqqq'
path = '/usr/local/BADNET-V3-relay/'

Counter = 1
relaySet = []


# ============ Registration ============

def relayRegistrationCheck():
    flag = contract_instance.functions.relay_registration_check().call({'from': account.wallet_addr})
    return 1 if flag else 0


def relayRegister():
    start = time.time()
    txn = contract_instance.functions.relay_register().buildTransaction(
        {
            'chainId': 5,
            'nonce': web3.eth.getTransactionCount(account.wallet_addr),
            'gas': 3000000,
            'value': Web3.toWei(0, 'ether'),
            'gasPrice': web3.eth.gasPrice,
        }
    )
    signed_txn = web3.eth.account.signTransaction(txn, private_key=account.wallet_private_key)
    result = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    txn_receipt = web3.eth.waitForTransactionReceipt(result, timeout=600)
    end = time.time()
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start))
    with open(path + 'log/blockchain.log', mode='a') as filename:
        filename.write(account.wallet_addr + ',' + str(dt) + ',relay_register,' + str(end-start) + '\n')
    return txn_receipt


# ============ Fetch the set of healthy relays (for encryption/decryption) ============

def relayGetIndexSet():
    return contract_instance.functions.relay_get_index_set().call({'from': account.wallet_addr})


def relayGetCurrentCounter():
    return contract_instance.functions.relay_get_current_counter().call({'from': account.wallet_addr})


def relayGetSet():
    relayTotalNum, UnhealthySet = relayGetIndexSet()
    global relaySet
    relaySet = []
    for i in range(1, relayTotalNum):
        if i not in UnhealthySet:
            relaySet.append(i)
    global Counter
    Counter = relayGetCurrentCounter()
    return Counter, relaySet


# ============ SRI Encryption & Upload ============

def padding(text):
    block_size = 16
    remainder = len(text.encode('utf-8')) % block_size
    if remainder:
        padding_needed = block_size - remainder
    else:
        padding_needed = 0
    text = text + ('\0' * padding_needed)
    return text.encode('utf-8')


def AES_encrypt(plain_text, key):
    mode = AES.MODE_CBC
    iv = AES_CBC_IV
    padded_text = padding(plain_text)
    cryptos = AES.new(key, mode, iv)
    cipher_text = cryptos.encrypt(padded_text)
    return binascii.hexlify(cipher_text)


def relayUploadSRIAndNSD(_Counter, Hdr, SRI, Key):
    _HDR = "0x" + Hdr
    AES_key = Key[0:32].encode('utf-8')
    _enSRI = "0x" + AES_encrypt(SRI, AES_key).decode()
    _NSD = "0x" + hashlib.sha256(SRI.encode()).hexdigest()

    start = time.time()
    txn = contract_instance.functions.relay_upload_SRI_and_NSD(_Counter, _HDR, _enSRI, _NSD).buildTransaction(
        {
            'chainId': 5,
            'nonce': web3.eth.getTransactionCount(account.wallet_addr),
            'gas': 3000000,
            'value': Web3.toWei(0, 'ether'),
            'gasPrice': web3.eth.gasPrice,
        }
    )
    signed_txn = web3.eth.account.signTransaction(txn, private_key=account.wallet_private_key)
    result = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    txn_receipt = ""
    try:
        txn_receipt = web3.eth.waitForTransactionReceipt(result, timeout=300)
    except TimeoutError:
        with open(path + 'log/blockchain.log', mode='a') as filename:
            filename.write('Timeout\n')
    else:
        end = time.time()
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start))
        with open(path + 'log/blockchain.log', mode='a') as filename:
            filename.write(account.wallet_addr + ',' + str(dt) + ',relay_upload_SRI_and_NSD,' + str(end-start) + '\n')
    return txn_receipt


# ============ SRI Download & Decryption  ============

def relayGetCounterList(index):
    operation, alterSet = contract_instance.functions.relay_get_counter_list(index).call({'from': account.wallet_addr})
    addSet = []
    deleteSet = []
    for i in range(0, len(operation)):
        if operation[i]:
            deleteSet += alterSet[i]
        else:
            addSet += alterSet[i]
    return addSet, deleteSet


def relayDownloadSRIHelper(index):
    counter, Hdr, enSRI = contract_instance.functions.relay_download_SRI(index).call({'from': account.wallet_addr})
    return counter, Hdr.hex(), enSRI.hex()


def relayDownloadSRI(relayID):
    relayCounter, Hdr, relayEnSRI = relayDownloadSRIHelper(relayID)
    S = relaySet.copy()
    if relayCounter < Counter:
        addSet, deleteSet = relayGetCounterList(relayCounter)
        for i in range(0, len(addSet)):
            S += addSet[i]
        for j in range(0, len(deleteSet)):
            S.remove(deleteSet[j])
    relayHdr = re.findall(r'.{130}', Hdr)
    return S, relayHdr, relayEnSRI


def AES_decrypt(cipher_text, key):
    mode = AES.MODE_CBC
    iv = AES_CBC_IV
    cryptos = AES.new(key, mode, iv)
    plain_text = cryptos.decrypt(binascii.a2b_hex(cipher_text))
    return bytes.decode(plain_text).rstrip('\0')


def relayDecryptSRIs(relayID, enSRI, decKey, fileEnd):
    AES_Key = bytes(decKey[0:32].encode())
    _SRI = AES_decrypt(enSRI, AES_Key)
    with open(path + 'lib/NIME-cached', mode='a') as filename:
        filename.write(str(relayID) + '\n')
        filename.write(_SRI + '\n')
    if fileEnd == 1:
        if os.path.exists(path + 'lib/NIME'):
            os.remove(path + 'lib/NIME')
        os.rename(path + 'lib/NIME-cached', path + 'lib/NIME')
