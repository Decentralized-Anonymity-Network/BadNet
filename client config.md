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
