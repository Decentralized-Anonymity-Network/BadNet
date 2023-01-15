# 测试人员
zx

# 测试时间
20210802-20210807

# 测试文档
../test/测试文档_stage1__(20210802-20210807).md

# 测试结果

## 客户端程序
- 数量：1台
- 类型：VMware
- 操作系统版本：CentOS-7.9
- 部署结果：成功
- 部署过程：

遇到的问题1：unzip BADNet.zip时报错

解决方法：将解压好的文件夹拖入虚拟机


遇到的问题2：运行curl报错：
```
“curl: (7) Can't complete SOCKS5 connection to 0.0.0.0:0. (6)”
```

解决方法：替换src/feature/nodelist/networkstatus.c，重新编译并运行

遇到的问题3：
```
[root@localhost app]# curl --socks5 127.0.0.1:9550 http://checkip.amazonaws.com/
curl: (7) Can't complete SOCKS5 connection to 0.0.0.0:0. (6)

[root@localhost app]# curl --socks5 127.0.0.1:9550 http://checkip.amazonaws.com/
curl: (7) Failed to receive SOCKS5 connect request ack.
```
解决方法：多等一个周期后（1h以后）再次运行curl行即可


## 注册账号

- 序号，账号，通信次数
- 1，0xAeDb6dB3552C22152cad6117cC8be44f20a8025c，10
- 2，0x9286f67aDC0BE0aaED01C87Cd9799613faA03f21，10
- 3，0x2147B8ab6B42a859D917Fe9f9F645ED8411F35D7，10
- 4，0xFF71C5674eC5BFb5083bb033641D16d7207601e7，10
- 5，0x2f53205489e214caeDeB3a0a53e781B6DAEAe9a7，10
- 6，0xa5D650D9ee53a3B7EE0be89c444613e81AA742f9，10
- 7，0x0451EbD41F41ae8ab5B4AeB3C48A775905a7046C，10
- 8，0x9267215EF3B6178B5F18944508E4c9EB9F73f0c5，10
- 9，0xaae0900e8e0aC91F34DcCcb241258a4F12Da09Ba，10
- 10，xxx，10
- 11，xxx，10
- 12，xxx，10
- 13，xxx，10
- 14，xxx，10
- 15，xxx，10
- 16，xxx，10
- 17，xxx，10
- 18，xxx，10
- 19，xxx，10
- 20，xxx，10
