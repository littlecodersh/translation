## TranslateError

以下两种情况将会抛出`TranslationError`：
* 使用了错误的指定翻译（仅支持谷歌、有道、百度、金山）
* 使用了错误的语言flag

*使用了错误的制定翻译*

```python
from translation import get, TranslateError

try:
    print(get('hello', default = 'humanbrain', dst = 'zh'))
except TranslateError as e:
    print(e.message)

# 将会显示：No such translation: humanbrain
```

*使用了错误的语言flag*

```python
from translation import get, TranslateError

try:
    print(get('hello', default = 'baidu', dst = 'zh-CN'))
except TranslateError as e:
    print(e.message)

# 将会显示：No language flag in baidu named: zh-CN
# 这是因为baidu这里官方认可的中文的简称为`zh`，我这里未作修改
```

## ConnectError

以下两种情况会抛出`ConnectError`
* 无法连接网络或者网络连接时间过长
* 代理服务器不可用

*无法连接网络或者网络连接时间过长*

```python
# 比如拔掉了网线以后 = =

from translation import get, ConnectError

try:
    print(get('hello world!', default = 'baidu', dst = 'zh'))
except ConnectError as e:
    print(e.message)

# 会显示：
# HTTPConnectionPool(host='fanyi.baidu.com', port=80): Max retries exceeded
# with url: /v2transapi (Caused by NewConnectionError('<requests.packages.u
# rllib3.connection.HTTPConnection object at 0x027D7350>: Failed to establi
# sh a new connection: [Errno 11001] getaddrinfo failed',))
```

*代理服务器不可用*

```python
# 比如 127.0.0.1:9012 不是你的代理端口

from translation import get, ConnectError

try:
    print(get('hello world!', default = 'baidu', dst = 'zh', proxies = {'http': '127.0.0.1:9012'}))
except ConnectError as e:
    print(e.message)

# 会显示：
# HTTPConnectionPool(host='127.0.0.1', port=9012): Max retries exceeded with url:
# http://fanyi.baidu.com/v2transapi (Caused by ProxyError('Cannot connect to proxy
# .', NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection obj
# ect at 0x027AD410>: Failed to establish a new connection: [Errno 10061] ',)))
