#!/bin/sh

path=`pwd`
aclocal
autoconf
autoheader
automake
mkdir -p /usr/local/BADNET-V3-relay/lib/keys
cp -r src/SC/ /usr/local/BADNET-V3-relay
cd ..
cp BADNET.relay /usr/local/BADNET-V3-relay
mkdir -p /usr/local/BADNET-V3-relay/log
cd /usr/local/BADNET-V3-relay/log/
touch notice.log info.log debug.log blockchain.log
cd /usr/local/BADNET-V3-relay/SC
python3 configure.py
cd $path
