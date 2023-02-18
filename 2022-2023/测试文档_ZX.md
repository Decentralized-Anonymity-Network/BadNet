## 测试结果
#### 客户端部署
- 客户端数量：1台
- 操作系统版本：CentOS 7.9
- 部署结果：成功
- 部署过程是否存在问题：
  
```
步骤 Running Google Chrome 报错：
[66800:66800:0218/003122.050213:ERROR:zygote_host_impl_linux.cc(100)] Running as root without --no-sandbox is not supported. See https://crbug.com/638180.
解决方法：
切换当前用户为非root用户，再运行该步骤即可
```
#### 可行性测试
序号   | 测试时间 | 访问网站 | 访问类型 | 访问情况
:---: | :----: | :----: | :----: | :----:
1 | 20230218 | youtube.com | 视频浏览 | 流畅
2 | 20230218 | facebook.com | 论坛浏览 | 流畅
3 | 20230218 | wikipedia.org | 百科 | 流畅
4 | 20230218 | reddit.com | 社交新闻 | 卡顿
5 | 20230218 | google.com | 搜索引擎 | 流畅
6 | 20230218 | amazon.com | 购物网站 | 流畅
7 | 20230218 | bbc.co.uk | 新闻 | 流畅
8 | 20230218 | indeed.com | 招聘信息 | 卡顿
9 | 20230218 |  wordpress.com | 博客 | 流畅
10 | 20230218 | torproject.org  | 匿名工具官网 | 流畅
11 | 20230218 | whatsapp.com  | 社交软件 | 流畅
12 | 20230218 | twitter.com | 社交软件 | 流畅
13 | 20230218 | yahoo.com | 门户网站 | 流畅
14 | 20230218 | tiktok.com | 短视频 | 卡顿
15 | 20230218 | ebay.com | 购物网站 | 流畅
16 | 20230218 | restaurantguru.com| 美食外卖 | 流畅
17 | 20230218 | apple.com | 购物网站 | 流畅
18 | 20230218 | instagram.com | 社交分享 | 流畅

#### 带宽测试
| 序号 | 测试时间 | 常规带宽 | BADNET带宽 |  
| :---:| :----: | :----: | :----: |
| 1 | 20230218 | 84Mbps | 2.3Mbps |
| 2 | 20230218 | 89Mbps | 4.9Mbps |
