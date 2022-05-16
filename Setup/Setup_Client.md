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
sudo sh badnet.sh (Note that output is an Ethereum address)
sudo ./configure
sudo make
```

Get rETH (Ropsten Ether) with generated address from 
[Faucet1](https://faucet.dimensions.network/), [Faucet2](https://faucet.egorfine.com/), or [Faucet3](https://faucet.metamask.io/).

#### Running BADNet client
```bat
cd src/app
sudo ./tor -f /usr/local/BADNet-client/BADNet.client
```

Normally, after waiting for one periods (i.e., 1 hour) to ensure that MSRI has content, the client can start using BADNet for anonymous communication. (Unfortunately,  this process may take more time due to the instability of the Ropsten Testnet.)
```bat
sudo cat /usr/local/BADNet-client/lib/MSRI
```

#### Using BADNET in Google Chrome
Install Google Chrome (If already installed, please ignore)
```bat
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
sudo yum localinstall google-chrome-stable_current_x86_64.rpm
```

Running Google Chrome
```bat
google-chrome --proxy-server=socks5://127.0.0.1:9550
```
