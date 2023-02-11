## 测试人员

ZJX

## 测试时间

2023/2/10

## 测试结果

### 客户端部署

- 问题1

```
运行google出现问题/usr/bin/google-chrome: symbol lookup error: /usr/bin/google-chrome: undefined symbol: gbm_bo_get_modifier
解决方法：
  输入yum install mesa-libgbm后输入
  google-chrome --no-sandbox --proxy-server=socks5://127.0.0.1:9550
错误原因：
  缺少libgbm库
  ```

- 问题2

```
输入sudo make报错make： ***[all] 错误 2
解决方法：
  将sudo ./configure --with-zlib-dir=/usr/lib替换成sudo ./configure --with-zlib-dir=/usr/lib --disable-asciidoc，再执行sudo make
  ```

### 可行性测试

| 序号 | 测试时间 | 访问网站    | 访问类型 | 访问情况   |
| ---- | -------- | ----------- | -------- | ---------- |
| 1    | 20230210 | Pinterest     | 社交网站     | 卡顿     |
| 2    | 20230210 | Amazon      | 购物     | 流畅     |
| 3    | 20230210 | Google      | 搜索引擎 | 流畅       |
| 4    | 20230210 | Wikipedia         | 百科 | 流畅     |
| 5    | 20230210 | Youtube     | 视频网站 | 卡顿 |
| 6    | 20230210| YellowPages | 黄页     | 流畅       |

### 带宽测试

| 序号 | 测试时间 | 常规带宽 | BADNET带宽 |
| ---- | -------- | -------- | ---------- |
| 1    | 20230126 | 56.36Mbps   | 0.53Mbps    |

