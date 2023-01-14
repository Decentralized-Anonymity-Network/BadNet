from web3 import Web3, HTTPProvider

import contract_abi
import account
import binascii
from Crypto.Cipher import AES
from ecies import decrypt

web3 = Web3(HTTPProvider("https://sepolia.infura.io/v3/67631e6ab6fc44e49915da74fd957740"))
contract_instance = web3.eth.contract(address=account.contract_address, abi=contract_abi.abi)
path = '/usr/local/BADNET-V3-client/'


def clientDownloadNSD():
    filePath = path + "lib/NSD"

    NSDIndex, _NSD = contract_instance.functions.client_download_NSD().call()
    NSD = binascii.hexlify(_NSD)

    with open(filePath, mode='w') as filename:
        local = 0
        for relayID in range(0, len(NSDIndex)):
            if NSDIndex[relayID]:
                filename.write(str(relayID+1) + ' ')
                SRIHash = NSD[local*64:(local+1)*64]
                filename.write(SRIHash.decode() + '\n')
                local += 1
