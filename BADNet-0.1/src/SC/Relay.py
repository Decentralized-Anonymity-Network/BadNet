from web3 import Web3, HTTPProvider

import contract_abi
import account
import binascii

web3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/67631e6ab6fc44e49915da74fd957740"))
contract_instance = web3.eth.contract(address=account.contract_address, abi=contract_abi.abi)


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


def relay_download_clients_public_keys():
    hex_string = contract_instance.functions.relay_download_clients_public_keys().call({'from': account.wallet_addr})
    return binascii.unhexlify(hex_string.encode('utf-8')).decode('utf-8')


def relay_upload_SRI_and_keys(string, keys):
    hex_string = binascii.hexlify(string.encode('utf-8')).decode('utf-8')
    # hex_keys = binascii.hexlify(keys.encode('utf-8')).decode('utf-8')
    txn = contract_instance.functions.relay_upload_SRI_and_keys(hex_string, "0x").buildTransaction(
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
