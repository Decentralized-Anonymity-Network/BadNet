import binascii
from ecies.utils import generate_key
from eth_account import Account


if __name__ == '__main__':
    secp_k = generate_key()
    wallet_private_key = binascii.hexlify(secp_k.secret).decode('utf-8')
    public_key = secp_k.public_key.format(True)
    wallet_public_key = binascii.hexlify(public_key).decode('utf-8')
    account = Account.from_key(wallet_private_key)
    wallet_addr = account.address

    with open('account.py', mode='a') as filename:
        filename.write('wallet_addr = "' + wallet_addr + '"' + '\n')
        filename.write('wallet_public_key = "' + wallet_public_key + '"' + '\n')
        filename.write('wallet_private_key = "' + wallet_private_key + '"' + '\n')

    print(wallet_addr)
