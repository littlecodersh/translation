import re, time, json

import requests

BASE_URL = 'http://www.iciba.com/index.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0', }
params = {
    'callback' : 'jQuery183041155304097723566_1468758748486',
    'a'        : 'getWordMean',
    'c'        : 'search',
    'list'     : '1,7,17',
    'word'     : None,
    '_'        : time.time() * 1e3, }

def iciba(text, src, dst, proxies):
    params['word'] = requests.utils.quote(requests.utils.quote(text.encode('utf8')))
    r = requests.get(BASE_URL, params, headers = headers, proxies = proxies)
    j = json.loads(re.findall('\(({.*})\)$', r.text)[0])
    return j['baesInfo']['translate_result']

if __name__ == '__main__':
    print(iciba('this is a test', 'auto', 'zh-CN', {}))
