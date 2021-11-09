from web3 import Web3, HTTPProvider

import contract_abi
import account
import binascii
import time
from Crypto.Cipher import AES
import secrets
from ecies import encrypt

web3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/f082b3f35d3a415b991b852a4ed0dccb"))
contract_instance = web3.eth.contract(address=account.contract_address, abi=contract_abi.abi)
AES_CBC_IV = b'qqqqqqqqqqqqqqqq'


def relay_registration_check():
    return contract_instance.functions.relay_registration_check().call({'from': account.wallet_addr})


def relay_register():
    start = time.time()
    txn = contract_instance.functions.relay_register().buildTransaction(
        {
            'chainId': 3,
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
    with open('/usr/local/BADNet-relay/log/blockchain.log', mode='a') as filename:
        filename.write(account.wallet_addr + ',' + str(dt) + ',relay_register,' + str(end-start) + '\n')
    return txn_receipt


def relay_get_clientlist_length():
    return contract_instance.functions.relay_get_clientlist_length().call({'from': account.wallet_addr})


def relay_download_clients_public_keys(i):
    hex_string = contract_instance.functions.relay_download_clients_public_keys(i).call({'from': account.wallet_addr})
    string = binascii.hexlify(hex_string).decode('utf-8')
    return bytearray(string.encode())


def relay_upload_SRI_and_keys(SRI, publicKey):
    AES_key = ''.join(secrets.token_hex(16)).encode('utf-8')
    encryptedSRI = AES_encrypt(SRI, AES_key)
    length = len(publicKey)
    encrypted_AES_Key = [0] * length
    if length > 0:
        for i in range(0, length):
            encrypted_AES_Key[i] = binascii.hexlify(encrypt(publicKey[i].decode(), AES_key))
        if length <= 5:
            temp = length
            encrypted_AES_Key_upload = encrypted_AES_Key
        else:
            temp = 5
            encrypted_AES_Key_upload = [0] * temp
            for j in range(0, 5):
                encrypted_AES_Key_upload[j] = encrypted_AES_Key[j]
    else:
        temp = 0
        encrypted_AES_Key_upload = [b'0x']

    start = time.time()
    txn = contract_instance.functions.relay_upload_SRI_and_keys(encryptedSRI, temp, encrypted_AES_Key_upload).buildTransaction(
        {
            'chainId': 3,
            'nonce': web3.eth.getTransactionCount(account.wallet_addr),
            'gas': 8000000,
            'value': Web3.toWei(0, 'ether'),
            'gasPrice': web3.eth.gasPrice,
        }
    )
    signed_txn = web3.eth.account.signTransaction(txn, private_key=account.wallet_private_key)
    result = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    try:
        txn_receipt = web3.eth.waitForTransactionReceipt(result, timeout=300)
    except Exception as e:
        with open('/usr/local/BADNet-relay/log/blockchain.log', mode='a') as filename:
            filename.write('Timeout\n')
    else:    
        end = time.time()
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start))
        with open('/usr/local/BADNet-relay/log/blockchain.log', mode='a') as filename:
            filename.write(account.wallet_addr + ',' + str(dt) + ',relay_upload_SRI_and_keys,' + str(end-start) + '\n')

    if length > 5:
        key_length = length - 5
        num = 1
        while key_length > 0:
            if key_length > 10:
                temp = 10
            else:
                temp = key_length
            encrypted_AES_Key_upload = [0] * temp
            for j in range(0, temp):
                encrypted_AES_Key_upload[j] = encrypted_AES_Key[num * 5 + j]
            
            start = time.time()
            txn = contract_instance.functions.relay_upload_keys(num, temp, encrypted_AES_Key_upload).buildTransaction(
                {
                    'chainId': 3,
                    'nonce': web3.eth.getTransactionCount(account.wallet_addr),
                    'gas': 8000000,
                    'value': Web3.toWei(0, 'ether'),
                    'gasPrice': web3.eth.gasPrice,
                }
            )
            signed_txn = web3.eth.account.signTransaction(txn, private_key=account.wallet_private_key)
            result = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            txn_receipt = web3.eth.waitForTransactionReceipt(result, timeout=300)
            end = time.time()
            dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start))
            with open('/usr/local/BADNet-relay/log/blockchain.log', mode='a') as filename:
                filename.write(account.wallet_addr + ',' + str(dt) + ',relay_upload_keys,' + str(end-start) + '\n')

            key_length = key_length - 10
            num = num + 2

    return txn_receipt


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

