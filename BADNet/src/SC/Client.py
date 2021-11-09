from web3 import Web3, HTTPProvider

import contract_abi
import account
import binascii
from Crypto.Cipher import AES
from ecies import decrypt

web3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/f082b3f35d3a415b991b852a4ed0dccb"))
contract_instance = web3.eth.contract(address=account.contract_address, abi=contract_abi.abi)
AES_CBC_IV = b'qqqqqqqqqqqqqqqq'


def client_registration_check():
    return contract_instance.functions.client_registration_check().call({'from': account.wallet_addr})


def client_register():
    txn = contract_instance.functions.client_register(account.wallet_public_key).buildTransaction(
        {
            'chainId': 3,
            'nonce': web3.eth.getTransactionCount(account.wallet_addr),
            'gas': 1000000,
            'value': Web3.toWei(0, 'ether'),
            'gasPrice': 10000000000,
        }
    )
    signed_txn = web3.eth.account.signTransaction(txn, private_key=account.wallet_private_key)
    result = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    txn_receipt = web3.eth.waitForTransactionReceipt(result, timeout=600)
    return txn_receipt


def client_get_RIAlength():
    return contract_instance.functions.client_get_RIAlength().call({'from': account.wallet_addr})


def client_get_current_RIA_length():
    return contract_instance.functions.client_get_current_RIA_length().call({'from': account.wallet_addr})


def client_generate_random_index():
    RIA_length = client_get_RIAlength()
    current_length = client_get_current_RIA_length()
    txn_receipt = ""
    while current_length < RIA_length:
        txn = contract_instance.functions.client_generate_random_index().buildTransaction(
            {
                'chainId': 3,
                'nonce': web3.eth.getTransactionCount(account.wallet_addr),
                'gas': 8000000,
                'value': Web3.toWei(0, 'ether'),
                'gasPrice': 10000000000,
            }
        )
        signed_txn = web3.eth.account.signTransaction(txn, private_key=account.wallet_private_key)
        result = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        txn_receipt = web3.eth.waitForTransactionReceipt(result, timeout=600)
        current_length = client_get_current_RIA_length()
    return txn_receipt


def client_download_MSRI(i):
    try:
        encrypted_key = contract_instance.functions.client_download_encrypted_keys(i).call({'from': account.wallet_addr})
        AES_Key = decrypt(account.wallet_private_key, binascii.unhexlify(encrypted_key))
        encrypted_SRI = contract_instance.functions.client_download_MSRI(i).call({'from': account.wallet_addr})
        SRI = AES_decrypt(encrypted_SRI, AES_Key)
    except ValueError:
        return bytearray(b'')
    else:
        return bytearray(SRI.encode())


def client_delete_random_index():
    txn = contract_instance.functions.client_delete_random_index().buildTransaction(
        {
            'chainId': 3,
            'nonce': web3.eth.getTransactionCount(account.wallet_addr),
            'gas': 8000000,
            'value': Web3.toWei(0, 'ether'),
            'gasPrice': 10000000000,
        }
    )
    signed_txn = web3.eth.account.signTransaction(txn, private_key=account.wallet_private_key)
    result = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    txn_receipt = web3.eth.waitForTransactionReceipt(result, timeout=600)
    return txn_receipt


def AES_decrypt(cipher_text, key):
    mode = AES.MODE_CBC
    iv = AES_CBC_IV
    cryptos = AES.new(key, mode, iv)
    plain_text = cryptos.decrypt(binascii.a2b_hex(cipher_text))
    return bytes.decode(plain_text).rstrip('\0')

