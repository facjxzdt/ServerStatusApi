ServerStatusApi
=================
使用FastApi实现的探针API
-----------------
>Python>=3.9

### 如何使用：

服务端：

1.安装必备库
```
pip install "fastapi[all]",logger
```
2.克隆本项目，并配置`api`目录下的`config.json`
```json
{
  "Password": "123456",
}
```
`Password`字段填写你想设置的密码

3.直接运行

`python api.py`

api默认监听`8000`端口，请确保该端口打开

客户端：

1.安装必备库

`pip install psutil,request,logger`

2.克隆本项目，并配置`agent`目录下的`config.json`

```json
{
  "Server": "http://127.0.0.1:8000",
  "Password": "123456",
  "Version": "v0.1",
  "Name": "test",
  "Time": 2
}
```

`Server`:配置服务端api地址

`Password`:配置密码(同服务端)

`Name`:配置机器名称(英文)

`Time`:回传间隔时间，单位s

3.直接运行

`python main.py`

### Api接口说明
1.`/info/based/{machine}`:获取名称为{machine}机器的系统信息

参数:

`?secret=`:服务端密匙

示例:
`/info/based/test?secret=123456`

返回：

```json
{
	"cpu_count": 6,
	"cpu_count_logical": 12,
	"mem_gb": 15.9,
	"mem_mb": 16309.6,
	"processor": "AMD64 Family 23 Model 113 Stepping 0, AuthenticAMD",
	"system": "Windows-10-10.0.22000-SP0",
	"system_v": "Windows"
}
```

2.`/info/based/{machine}`:获取名称为{machine}机器的系统信息

参数:

`?secret=`:服务端密匙

示例:
`/info/device/test?secret=123456`

返回：
```json
{
	"bytes_rcvd": "20.47 Mb",
	"bytes_sent": "378.43 Mb",
	"cpu_usage": 0.0,
	"free_disk": 252.4,
	"mem_used": 8110.9,
	"total_disk": 1599.8999999999999,
	"used_disk": 1347.3
}
```

### TODO:
* 添加websocket通信
* WEBUI
* WOL唤醒
* 米家插座唤醒
