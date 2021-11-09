from web3 import Web3, HTTPProvider

import contract_abi
import account
import binascii
from Crypto.Cipher import AES
import secrets
from ecies import encrypt

web3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/67631e6ab6fc44e49915da74fd957740"))
contract_instance = web3.eth.contract(address=account.contract_address, abi=contract_abi.abi)
AES_CBC_IV = b'qqqqqqqqqqqqqqqq'


def relay_registration_check():
    return contract_instance.functions.relay_registration_check().call({'from': account.wallet_addr})


def relay_register():
    txn = contract_instance.functions.relay_register().buildTransaction(
        {
            'chainId': 3,
            'nonce': web3.eth.getTransactionCount(account.wallet_addr),
            'gas': 800000,
            'value': Web3.toWei(0, 'ether'),
            'gasPrice': web3.eth.gasPrice,
        }
    )
    signed_txn = web3.eth.account.signTransaction(txn, private_key=account.wallet_private_key)
    result = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    txn_receipt = web3.eth.waitForTransactionReceipt(result, timeout=600)
    return txn_receipt


def relay_get_clientlist_length():
    return contract_instance.functions.relay_get_clientlist_length().call({'from': account.wallet_addr})


def relay_download_clients_public_keys(i):
    hex_string = contract_instance.functions.relay_download_clients_public_keys(i).call({'from': account.wallet_addr})
    string = binascii.hexlify(hex_string).decode('utf-8')
    return bytearray(string.encode())


def relay_upload_SRI_and_keys(SRI, publicKey, is_publickeys):
    AES_key = ''.join(secrets.token_hex(16)).encode('utf-8')
    encryptedSRI = AES_encrypt(SRI, AES_key)
    if is_publickeys == 1:
        length = len(publicKey)
        encrypted_AES_Key = [0] * length
        for i in range(0, length):
            encrypted_AES_Key[i] = binascii.hexlify(encrypt(publicKey[i].decode(), AES_key))
    else:
        encrypted_AES_Key = [b'0x']
    txn = contract_instance.functions.relay_upload_SRI_and_keys(encryptedSRI, encrypted_AES_Key).buildTransaction(
        {
            'chainId': 3,
            'nonce': web3.eth.getTransactionCount(account.wallet_addr),
            'gas': 800000,
            'value': Web3.toWei(0, 'ether'),
            'gasPrice': web3.eth.gasPrice,
        }
    )
    signed_txn = web3.eth.account.signTransaction(txn, private_key=account.wallet_private_key)
    result = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    txn_receipt = web3.eth.waitForTransactionReceipt(result, timeout=600)
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

