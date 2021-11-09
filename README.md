# Overview
BADNet is a decentralized anonymity network based on blockchain and smart contracts, which makes use of two open source projects, Tor and Ethereum.

# BADNet-0.1
BADNet (version 0.2) is build based on Tor version 0.4.6.5 and Ropsten Ethereum Testnet. Specifically, circuit-related operations are derived from Tor source code, but Tor Directory Authority is replaced by DDA written in Solidity, and DDA's code is in "Directory.sol".

- Contract Address: [0x376b3bc1c18809600ae5f0d9d82dbea8f31525cb](https://ropsten.etherscan.io/address/0x376b3bc1c18809600ae5f0d9d82dbea8f31525cb)
- Deployment Date: July 20, 2021
- Status: discontinued operations as of August 10, 2021
- Total Number of Transactions: 4,427 (All transactions are recorded in "transaction_data")

## Dependencies (Centos):
```bat
yum install libevent-devel openssl-devel python36 python36-devel -y
sudo ln -s /usr/lib64/libpython3.6m.so.1.0 /usr/lib/libpython3.6.so
pip3 install --upgrade pip
pip3 install web3 eciespy
```

## Setup:
```bat
cd BADNet-0.2
aclocal
autoconf
autoheader
automake
./configure
make
```

```bat
mkdir -p /usr/local/etc/BADNet
cp BADNet.client /usr/local/etc/BADNet/
mkdir -p /usr/local/BADNet/lib/keys
mkdir -p /usr/local/BADNet/log
cd /usr/local/BADNet/log/
touch notice.log info.log debug.log
```

## Create a Ropsten Ethereum account:
```bat
cd BADNet-0.2/src/SC/
python3 create_account.py (output is the client address)
```
[Ropsten Ethereum (rETH) Faucet](https://faucet.dimensions.network/)

## Running BADNet:
```bat
cd BADNet-0.2/src/app/
./tor -f /usr/local/etc/BADNet/BADNet.client
```
After waiting for a period (currently set to 1 hour), clients can start using BADNet for anonymous communication.
