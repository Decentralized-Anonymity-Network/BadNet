from web3 import Web3, HTTPProvider

import contract_abi
import account
import binascii
from Crypto.Cipher import AES
from ecies import decrypt

web3 = Web3(HTTPProvider("https://goerli.infura.io/v3/67631e6ab6fc44e49915da74fd957740"))
contract_instance = web3.eth.contract(address=account.contract_address, abi=contract_abi.abi)
path = '/usr/local/BADNET-V3-client/'


def clientDownloadNSD():
    filePath = path + "lib/NSD"
    if os.path.exists(filePath):
        os.remove(filePath)

    NSDIndex, _NSD = contract_instance.functions.client_download_NSD().call({'from': account.wallet_addr})
    NSD = binascii.hexlify(_NSD)

    local = 0
    for relayID in range(0, len(NSDIndex)):
        if NSDIndex[relayID]:
            with open(filePath, mode='a') as filename:
                filename.write(relayID +'\n')
                filename.write(NSD[local*64:(local+1)*64] +'\n')
                local += 1
