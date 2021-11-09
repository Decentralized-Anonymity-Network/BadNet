#!/bin/sh

path=`pwd`
aclocal
autoconf
autoheader
automake
mkdir -p /usr/local/BADNet-client/lib/keys
cp -r src/SC/ /usr/local/BADNet-client
cd ..
cp BADNet.client /usr/local/BADNet-client
mkdir -p /usr/local/BADNet-client/log
cd /usr/local/BADNet-client/log/
touch notice.log info.log debug.log
cd /usr/local/BADNet-client/SC
python3 configure.py client
cd $path
