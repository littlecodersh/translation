from translation import Translation, baidu, google, youdao, iciba, bing

print(baidu('hello world!', dst = 'zh'))
print(youdao('hello world!', dst = 'zh-CN'))
print(iciba('hello world!', dst = 'zh'))
print(google('hello world!', dst = 'zh-CN'))
print(bing('hello world!', dst = 'zh-CHS'))
