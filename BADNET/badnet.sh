#!/bin/sh

path=`pwd`
aclocal
autoconf
autoheader
automake
mkdir -p /usr/local/BADNET-V3-client/lib/keys
cp -r src/SC/ /usr/local/BADNET-V3-client
cd ..
cp BADNET.client /usr/local/BADNET-V3-client
mkdir -p /usr/local/BADNET-V3-client/log
cd /usr/local/BADNET-V3-client/log/
touch notice.log info.log debug.log
cd $path
