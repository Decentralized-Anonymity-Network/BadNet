#!/bin/sh

path=`pwd`
aclocal
autoconf
autoheader
automake
mkdir -p /usr/local/BADNet-relay/lib/keys
cp -r src/SC/ /usr/local/BADNet-relay
cd ..
cp BADNet.relay /usr/local/BADNet-relay
mkdir -p /usr/local/BADNet-relay/log
cd /usr/local/BADNet-relay/log/
touch notice.log info.log debug.log blockchain.log
cd /usr/local/BADNet-relay/SC
python3 configure.py relay
cd $path
