from translation import Translation, baidu, google, youdao, iciba

print(baidu('hello world!', dst = 'zh'))
print(google('hello world!', dst = 'zh-CN', proxies = {'http': '127.0.0.1:1080'}))
print(youdao('hello world!', dst = 'zh-CN'))
print(iciba('hello world!', dst = 'zh'))
