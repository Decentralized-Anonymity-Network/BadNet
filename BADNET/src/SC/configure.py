import sys
import binascii
from ecies.utils import generate_key
from eth_account import Account

from web3 import Web3, HTTPProvider
import contract_abi

contract_address = "0xe7BC117CE3439e32549115f049d3D17A17EC03c8"
web3 = Web3(HTTPProvider("https://goerli.infura.io/v3/67631e6ab6fc44e49915da74fd957740"))
contract_instance = web3.eth.contract(address=contract_address, abi=contract_abi.abi)
path = '/usr/local/BADNET-V3-relay/'


def relayCreateAccount(path):
    secp_k = generate_key()
    wallet_private_key = binascii.hexlify(secp_k.secret).decode('utf-8')
    public_key = secp_k.public_key.format(True)
    wallet_public_key = binascii.hexlify(public_key).decode('utf-8')
    account = Account.from_key(wallet_private_key)
    wallet_addr = account.address

    with open(path, mode='w') as filename:
        filename.write('contract_address = "' + contract_address + '"' + '\n\n')
        filename.write('wallet_addr = "' + wallet_addr + '"' + '\n')
        filename.write('wallet_public_key = "' + wallet_public_key + '"' + '\n')
        filename.write('wallet_private_key = "' + wallet_private_key + '"' + '\n')
    print(wallet_addr)


def relayGetUploadPeriod():
    return contract_instance.functions.relay_get_upload_period().call({'from': account.wallet_addr})


if __name__ == '__main__':
    relayCreateAccount(path + 'SC/account.py')
    RelayUploadPeriod = relayGetUploadPeriod()
    with open(path + 'BADNET.relay', mode='a') as filename:
        filename.write('\n' + 'RelayUploadPeriod ' + str(RelayUploadPeriod))
