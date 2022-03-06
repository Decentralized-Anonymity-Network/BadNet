## Requirements:
The prototype system installation requires CentOS/Ubuntu system and Python 3.6.

## Dependencies:
#### CentOS
```bat
sudo yum install gcc libevent-devel openssl-devel automake python36 python36-devel -y
sudo ln -s /usr/lib64/libpython3.6m.so.1.0 /usr/lib/libpython3.6.so
pip3 install --upgrade pip
pip3 install web3 eciespy
```
#### Ubuntu
```bat
sudo apt-get install gcc libevent-dev libssl-dev automake python3.6 python3.6-dev -y
sudo ln -s /usr/lib/python3.6/config-3.6m-x86_64-linux-gnu/libpython3.6.so /usr/lib/libpython3.6.so
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
cd BadNet
vi BADNet.relay (fill in "Nickname", "OrPort" and "Address")
cd BADNet
sudo sh badnet_relay.sh (output is a Ropsten Ethereum address)
sudo ./configure
sudo make
```

Get rETH (Ropsten Ethereum) with generated address from
[Faucet1](https://faucet.dimensions.network/), [Faucet2](https://teth.bitaps.com/), or [Faucet3](https://faucet.ropsten.be/).

#### Running BADNet relay:
```bat
cd src/app
sudo ./tor --list-fingerprint --orport 1 --dirserver "x 127.0.0.1:1 ffffffffffffffffffffffffffffffffffffffff" --datadirectory /usr/local/BADNet-relay/lib/
sudo ./tor -f /usr/local/BADNet-relay/BADNet.relay
```
