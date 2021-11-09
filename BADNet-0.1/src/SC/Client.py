from web3 import Web3, HTTPProvider

import contract_abi
import account

web3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/67631e6ab6fc44e49915da74fd957740"))
contract_instance = web3.eth.contract(address=account.contract_address, abi=contract_abi.abi)


def client_registration_check():
    return contract_instance.functions.client_registration_check().call({'from': account.wallet_addr})


def client_register():
    txn = contract_instance.functions.client_register(account.wallet_public_key).buildTransaction(
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
    return txn_receipt


def client_generate_random_index():
    txn = contract_instance.functions.client_generate_random_index().buildTransaction(
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
    return txn_receipt


def client_get_RIA_length():
    return contract_instance.functions.client_get_RIA_length().call({'from': account.wallet_addr})


def client_download_MSRI(i):
    hex_string = contract_instance.functions.client_download_MSRI(i).call({'from': account.wallet_addr})
    return bytearray(hex_string)


def client_download_encrypted_keys(i):
    hex_string = contract_instance.functions.client_download_encrypted_keys(i).call({'from': account.wallet_addr})
    return bytearray(hex_string)


def client_delete_random_index():
    txn = contract_instance.functions.client_delete_random_index().buildTransaction(
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
    return txn_receipt
