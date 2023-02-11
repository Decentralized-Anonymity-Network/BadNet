## 测试人员
WM

## 测试时间
20230210

## 测试结果
#### 客户端部署
- 客户端数量：1台
- 操作系统版本：CentOS 7.4
- 部署结果：成功
- 部署过程是否存在问题：

```
问题1：git clone https://github.com/Decentralized-Anonymity-Network/BadNet.git 克隆不到项目
解决方法：
重置代理
git config --global --unset http.proxy
git config --global --unset https.proxy
添加全局代理
git config --global http.proxy
git config --global https.proxy
```

#### 可行性测试
序号   | 测试时间 | 访问网站 | 访问类型 | 访问情况
:---: | :----: | :----: | :----: | :----:
1 | 20230210| Youtube | 视频浏览 | 卡顿
2 | 20230210| facebook.com | 论坛浏览 | 流畅
3 | 20230210| wikipedia.org | 百科 | 流畅
4 | 20230210| pinterest.com | 社交图片分享 | 卡顿
5 | 20230210| google.com | 搜索引擎 | 流畅
6 | 20230210| amazon.com | 购物网站 | 流畅
7 | 20230210| instagram.com | 社交图片分享 | 流畅
8 | 20230210| twitter.com | 社交软件 | 卡顿
9 | 20230210| tiktok.com | 短视频 | 卡顿
10 | 20230210 | ebay.com | 购物网站 | 流畅
11 | 20230210 | apple.com | 购物网站 | 流畅
12 | 20230210 | bbc.co.uk | 新闻 | 流畅
13 | 20230210 | reddit.com | 社交新闻 | 卡顿

#### 带宽测试
| 序号 | 测试时间 | 常规带宽 | BADNET带宽 |  
| :---:| :----: | :----: | :----: |
| 1 | 20230210 | 63Mbps | 44Mbps |
