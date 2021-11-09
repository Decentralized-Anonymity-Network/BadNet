# 1 测试内容
BADNet 实验（阿里云服务器）：使用浏览器进行网站访问测试

# 2 测试参数
20210910，hanyang

# 3 测试内容

## 3.1 浏览器访问 10 个网站，人工感觉延迟
https://www.wikipedia.org/ 4s

https://twitter.com/ 4s

https://www.reddit.com/ 5s

https://www.bbc.co.uk/ 5s

https://www.nytimes.com/ 3s

https://www.wsj.com/ 3s

https://www.torproject.org 5s

https://ropsten.etherscan.io/ 5s

https://www.google.com.hk/ 3s

https://www.instagram.com/ 5s 

## 3.2 curl 指令获取延迟时间数值
指令：e.g., curl --socks5 127.0.0.1:9550 -w %{time_total}"\n" "https://scholar.google.com/"

网站：

https://www.wikipedia.org/ 3.010s

https://twitter.com/ 3.186s

https://www.reddit.com/ 5.340s

https://www.bbc.co.uk/ 4.923s

https://www.nytimes.com/ 5.787s

https://www.wsj.com/ 5.446s

https://www.torproject.org 3.898s

https://ropsten.etherscan.io/ 2.920s

https://www.google.com.hk/ 2.732

https://www.instagram.com/ 2.636s 

# 4 实验体会

P.S. 猜测一些网站会对未知流量进行阻止。
（1）https://scholar.google.com/
... but your computer or network may be sending automated queries. To protect our users, we 
can't process your request right now.
（2）https://www.facebook.com/ or https://www.google.com/
浏览器访问显示“找不到网站。我们无法连接至 www.facebook.com 的服务器”。