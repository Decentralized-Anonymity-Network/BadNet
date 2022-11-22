## Requirements:
The prototype system installation requires CentOS/Ubuntu system and Python 3.6.

## Dependencies:
#### CentOS
```bat
sudo yum install gcc libevent-devel openssl-devel automake python36 python36-devel gmp-devel flex bison -y
sudo wget https://crypto.stanford.edu/pbc/files/pbc-0.5.14.tar.gz
tar -zxvf pbc-0.5.14.tar.gz
cd pbc-0.5.14 && ./configure && make && make install

sudo ln -s /usr/lib64/libpython3.6m.so.1.0 /usr/lib/libpython3.6.so
sudo ln -s /usr/lib64/libgmp.so.10 /usr/lib/libgmp.so.10
sudo ln -s /usr/local/lib/libpbc.so.1 /usr/lib/libpbc.so.1

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
vi BADNET.relay (fill in "Nickname", "OrPort" and "Address")
cd BADNET
sudo sh badnet_relay.sh (output is an Ethereum address)
sudo ./configure --disable-asciidoc
sudo make
```

Get ETH (Ethereum Goerli Testnet) with generated address from 
[Faucet1](https://ethdrop.dev/), [Faucet2](https://www.allthatnode.com/faucet/ethereum.dsrv), or [Faucet3](https://goerli-faucet.pk910.de/).

#### Running BADNET relay:
```bat
cd src/app
sudo ./tor --list-fingerprint --orport 1 --dirserver "x 127.0.0.1:1 ffffffffffffffffffffffffffffffffffffffff" --datadirectory /usr/local/BADNET-V3-relay/lib/
sudo ./tor -f /usr/local/BADNET-V3-relay/BADNET.relay
```
