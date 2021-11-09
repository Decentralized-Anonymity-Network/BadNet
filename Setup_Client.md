## Requirements:
The prototype system installation requires CentOS system and Python 3.6.

## Dependencies:
```bat
sudo yum install gcc libevent-devel openssl-devel automake python36 python36-devel -y
sudo ln -s /usr/lib64/libpython3.6m.so.1.0 /usr/lib/libpython3.6.so
pip3 install --upgrade pip
pip3 install web3 eciespy
```

## Setup:
#### Get BADNet
```bat
git clone https://github.com/Decentralized-Anonymity-Network/BadNet.git
```

#### Quick auto setup
```bat
cd BADNet
sudo sh badnet.sh (output is a Ropsten Ethereum address)
sudo ./configure
sudo make
```

obtain rETH (Ropsten Ethereum) with generated address from one of these faucet:
- https://faucet.dimensions.network/
- https://teth.bitaps.com/
- https://faucet.ropsten.be/

#### Running BADNet client
```bat
cd src/app
sudo ./tor -f /usr/local/BADNet-client/BADNet.client
```

After waiting for 1 to 2 periods to ensure that MSRI has content, the client can start using BADNet for anonymous communication.
```bat
sudo cat /usr/local/BADNet-client/lib/MSRI
```
