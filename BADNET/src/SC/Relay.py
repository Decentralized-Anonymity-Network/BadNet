from web3 import Web3, HTTPProvider
import contract_abi
import account

import time
import binascii
import hashlib
import zlib
from Crypto.Cipher import AES
import secrets
from ecies import encrypt
import os
import linecache

web3 = Web3(HTTPProvider("https://goerli.infura.io/v3/67631e6ab6fc44e49915da74fd957740"))
contract_instance = web3.eth.contract(address=account.contract_address, abi=contract_abi.abi)
AES_CBC_IV = b'qqqqqqqqqqqqqqqq'
path = '/usr/local/BADNET-V3-relay/'


# ============ 注册 ============

def relayRegistrationCheck():
    return contract_instance.functions.relay_registration_check().call({'from': account.wallet_addr})


def relayRegister():
    start = time.time()
    txn = contract_instance.functions.relay_register().buildTransaction(
        {
            'chainId': 5,
            'nonce': web3.eth.getTransactionCount(account.wallet_addr),
            'gas': 1000000,
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


# ============ 获取健康节点集合S（用于加/解密） ============

def relayGetIndexSet():
    return contract_instance.functions.relay_get_index_set().call({'from': account.wallet_addr})


def relayGetCurrentCounter():
    return contract_instance.functions.relay_get_current_counter().call({'from': account.wallet_addr})


def relayGetSet():
    relayTotalNum, UnhealthySet = relayGetIndexSet()
    relaySet = []
    for i in range(1, relayTotalNum):
        if i not in UnhealthySet:
            relaySet.append(i)
    Counter = relayGetCurrentCounter()
    return Counter, relaySet


# ============ 加密SRI&上传 ============

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


def relayUploadSRIAndNSD(_Counter, _HDR, _SRI, Key):
    AES_key = Key[0:32].encode('utf-8')
    _NSD = hashlib.sha256(_SRI.encode()).hexdigest()
    encryptedSRI = binascii.unhexlify(AES_encrypt(_SRI, AES_key))

    start = time.time()
    txn = contract_instance.functions.relay_upload_SRI_and_NSD(_Counter, _HDR, encryptedSRI, _NSD).buildTransaction(
        {
            'chainId': 5,
            'nonce': web3.eth.getTransactionCount(account.wallet_addr),
            'gas': 1000000,
            'value': Web3.toWei(0, 'ether'),
            'gasPrice': web3.eth.gasPrice,
        }
    )
    signed_txn = web3.eth.account.signTransaction(txn, private_key=account.wallet_private_key)
    result = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    txn_receipt = ""
    try:
        txn_receipt = web3.eth.waitForTransactionReceipt(result, timeout=600)
    except Exception as e:
        with open(path + 'log/blockchain.log', mode='a') as filename:
            filename.write('Timeout\n')
    else:
        end = time.time()
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start))
        with open(path + 'log/blockchain.log', mode='a') as filename:
            filename.write(account.wallet_addr + ',' + str(dt) + ',relay_upload_SRI_and_NSD,' + str(end-start) + '\n')
    return txn_receipt


# ============ 下载NIME&解密 ============

def relayGetCounterList(index):
    return contract_instance.functions.relay_get_counter_list(index).call({'from': account.wallet_addr})


def relayDownloadSRIHelper(index):
    try:
        counter, HdrTemp, encrypted_SRI = contract_instance.functions.relay_download_SRI(index).call({'from': account.wallet_addr})
        _Hdr = zlib.decompress(HdrTemp).decode()
        enSRI = binascii.hexlify(encrypted_SRI)
    except BaseException:
        return bytearray(b'')
    else:
        return counter, _Hdr, bytearray(enSRI)


def relayDownloadSRI():
    filePath = path + 'lib/NIME-enc'
    if os.path.exists(filePath):
        os.remove(filePath)

    Counter, relaySet = relayGetSet()
    for relayID in relaySet:
        relayCounter, relayHdr, relayEnSRI = relayDownloadSRIHelper(relayID)
        S = relaySet        
        if relayCounter < Counter:
            addSet = relayGetCounterList(relayCounter)
            for j in range(0, len(addSet)):
                S += addSet[j]
        with open(filePath, mode='a') as filename:
            filename.write(relayID +'\n')
            filename.write(S + '\n')
            filename.write(relayHdr + '\n')
            filename.write(relayEnSRI + '\n')


def AES_decrypt(cipher_text, key):
    mode = AES.MODE_CBC
    iv = AES_CBC_IV
    cryptos = AES.new(key, mode, iv)
    plain_text = cryptos.decrypt(binascii.a2b_hex(cipher_text))
    return bytes.decode(plain_text).rstrip('\0')


def relayDecryptNIME(sum, decKey):
    for num in range(1, sum+1):
        AES_Key = bytes(decKey[num-1][0:32].encode())
        relayID = linecache.getline(path + 'lib/NIME-enc', num*4-3).strip()
        enSRI = linecache.getline(path + 'lib/NIME-enc', num*4).strip()
        _SRI = AES_decrypt(enSRI, AES_Key)
        with open(path + 'lib/NIME-cached', mode='a') as filename:
            filename.write(relayID + '\n')
            filename.write(_SRI + '\n')
    
    filePath = path + 'lib/NIME'
    if os.path.exists(filePath):
        os.remove(filePath)
    os.rename(path + 'lib/NIME-cached', filePath)
