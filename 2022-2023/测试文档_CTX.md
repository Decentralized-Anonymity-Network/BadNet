## 测试结果
#### 客户端部署
- 客户端数量：1台
- 操作系统版本：CentOS7
- 部署结果：成功
- 部署过程是否存在问题：
  
```
存在问题：
在文档的Running Google Chrome中，遇到了undefined symbol: gbm_bo_get_modifier的问题，无法打开Chrome浏览器。
解决办法：
使用yum install mesa-libgbm ，再运行 google-chrome --no-sandbox --proxy-server=socks5://127.0.0.1:9550，Chrome浏览器就可以正常使用了。
```
#### 可行性测试
| 序号 | 测试时间 |   访问网站    |    访问类型    | 访问情况 |
| :--: | :------: | :-----------: | :------------: | :------: |
|  1   | 20230204 |  youtube.com  |    视频网站    |   卡顿   |
|  2   | 20230204 | facebook.com  |    社交网络    |   流畅   |
|  3   | 20230204 | wikipedia.org |    维基百科    |   流畅   |
|  4   | 20230204 | pinterest.com |    社交网络    |   卡顿   |
|  5   | 20230204 |  google.com   |    搜索引擎    |   流畅   |
|  6   | 20230204 |  amazon.com   |    购物网站    |   流畅   |
|  7   | 20230204 | instagram.com |    社交网站    |   流畅   |
|  8   | 20230204 |  twitter.com  |    社交网站    |   卡顿   |
|  9   | 20230204 | linkedin.com  |    职位应聘    |   流畅   |
|  10  | 20230204 |  reddit.com   |    社交新闻    |   卡顿   |
|  11  | 20230204 |  tiktok.com   |     短视频     |   卡顿   |
|  12  | 20230204 |   quora.com   |    问答SNS     |   卡顿   |
|  13  | 20230204 |   ebay.com    |    购物网站    |   流畅   |
|  14  | 20230204 |   etsy.com    | 销售手工工艺品 |   流畅   |
|  15  | 20230204 |   yahoo.com   |    门户网站    |   流畅   |
|  16  | 20230204 |   apple.com   |    苹果官网    |   流畅   |
|  17  | 20230204 |  fandom.com   |    协助编辑    |   卡顿   |
|  18  | 20230204 |   yelp.com    |  商户点评网站  |   卡顿   |
|  19  | 20230204 |  walmart.com  |   沃尔玛网站   |   流畅   |
|  20  | 20230204 | wordpress.com |    博客平台    |   卡顿   |

#### 带宽测试
| 序号 | 测试时间 |  常规带宽  | BADNET带宽 |
| :--: | :------: | :--------: | :--------: |
|  1   | 20230204 | 143.67Mbps |  2.58Mbps  |