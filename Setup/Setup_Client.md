## Requirements
The prototype system installation requires CentOS system and Python 3.6.

## Dependencies
```bat
sudo yum install gcc libevent-devel openssl-devel automake python36 python36-devel gmp-devel flex bison -y
wget https://crypto.stanford.edu/pbc/files/pbc-0.5.14.tar.gz
tar -zxvf pbc-0.5.14.tar.gz
cd pbc-0.5.14 && ./configure && make && sudo make install

sudo ln -s /usr/lib64/libpython3.6m.so.1.0 /usr/lib/libpython3.6.so
sudo ln -s /usr/lib64/libgmp.so.10 /usr/lib/libgmp.so.10
sudo ln -s /usr/local/lib/libpbc.so.1 /usr/lib/libpbc.so.1

pip3 install --upgrade pip
pip3 install web3 eciespy
```

## Setup
### Get BADNET
```bat
git clone https://github.com/Decentralized-Anonymity-Network/BadNet.git
```

### Quick auto setup
```bat
cd BadNet/BADNET
sudo sh badnet.sh
sudo ./configure
sudo make
```

### Running BADNET client
```bat
cd src/app
sudo ./tor -f /usr/local/BADNET-V3-client/BADNET.client
```

### Using BADNET in Google Chrome
Install Google Chrome (If already installed, please ignore)
```bat
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
sudo yum localinstall google-chrome-stable_current_x86_64.rpm
```

Running Google Chrome
```bat
google-chrome --proxy-server=socks5://127.0.0.1:9550
```
