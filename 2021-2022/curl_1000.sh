#!/bin/bash
# 修改 i 更改测试次数
echo "new test"
echo "new test" >>result1.txt
for ((i=1; i<=1000; i ++))
    do
    echo $i
		echo $i >>result1.txt
		echo -n ";"	>>result1.txt
		curl http://checkip.amazonaws.com/ -s -w ";"%{time_total}"\n" >>result1.txt
		echo -n ";" >>result1.txt
		curl --socks5 127.0.0.1:9550 http://checkip.amazonaws.com/ -s -w ";"%{time_total}"\n" >>result1.txt
		echo -n ";" >>result1.txt
		echo "http://checkip.amazonaws.com/" >>result1.txt
		sleep 3
done 
	