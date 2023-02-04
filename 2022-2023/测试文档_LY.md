## 测试人员

LY

## 测试时间

2023/2/4

## 测试结果

### 客户端部署

- 问题1

  ```golang
  Ping不通github.com
  解决方法：输入cd /后输入vim etc/hosts，点击a，在最后一行添加140.82.112.4 github.com，后点击esc键，输入：wq
  ```

- 问题2

  ```golang
  运行google出现问题/usr/bin/google-chrome: symbol lookup error: /usr/bin/google-chrome: undefined symbol: gbm_bo_get_modifier
  解决方法：输入yum install mesa-libgbm后输入google-chrome --no-sandbox --proxy-server=socks5://127.0.0.1:9550
  错误原因：缺少libgbm库
  ```
  
  - 问题3

  ```golang
  执行git clone https://github.com/Decentralized-Anonymity-Network/BadNet.git报错没有git命令
  解决方法：yum install git
  错误原因：缺少git库
  ```
  
  - 问题4

  ```golang
  浏览器输入网址无响应
  解决方法：终端输入curl --socks5 127.0.0.1:9550 http://checkip.amazonaws.com/
  ```
  
  - 问题5

  ```golang
  输入sudo make报错make： ***[all] 错误 2
  解决方法：
  将sudo ./configure --with-zlib-dir=/usr/lib替换成sudo ./configure --with-zlib-dir=/usr/lib --disable-asciidoc，再执行sudo make
  ```

### 可行性测试

| 序号 | 测试时间 | 访问网站    | 访问类型 | 访问情况   |
| ---- | -------- | ----------- | -------- | ---------- |
| 1    | 20230204 | youtube     | 视频网站     | 卡顿    |
| 2    | 20230204 | twitter      | 视频网站     | 流畅     |
| 3    | 20230204 | instagram      | 社交网站 | 严重卡顿       |
| 4    | 20230204 | amazon         | 购物网站 | 卡顿     |
| 5    | 20230204 | tiktok     | 视频网站 | 卡顿 |
| 6    | 20230204 | YellowPages | 黄页     | 卡顿       |
| 7    | 20230204 | facebook | 社交网站     | 流畅       |


### 带宽测试

| 序号 | 测试时间 | 常规带宽 | BADNET带宽 |
| ---- | -------- | -------- | ---------- |
| 1    | 20230204 | 52.54Mbps   | 1.65Mbps    |

