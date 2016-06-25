import re

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0', }

BASE_URL = 'http://www.iciba.com/'

def iciba(text, src, dst, proxies):
    r = requests.get(BASE_URL + text, headers = headers, proxies = proxies).text
    t = ';'.join([i.replace(' ', '').strip() for i in re.findall(
        '<li class="clearfix">[\s\S]*?<p>([^<]*?)</p>', r)])
    if t == '': return ''.join(re.findall(
        '<span class="base-word-long">([\s\S]*?)</span>', r))

if __name__ == '__main__':
    print(iciba('Test is test', 'auto', 'zh-CN', {}))
