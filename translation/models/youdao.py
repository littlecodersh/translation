import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0', }
BASE_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc'
params = {
    'i'          : None,
    'type'       : 'AUTO',
    'doctype'    : 'json',
    'xmlVersion' : '1.8',
    'keyfrom'    : 'fanyi.web',
    'ue'         : 'UTF-8',
    'action'     : 'FY_BY_CLICKBUTTON',
    'typoResult' : 'true', }

def youdao(text, src, dst, proxies):
    params['i'] = text
    return requests.post(BASE_URL, params, headers = headers, proxies = proxies
            ).json()['translateResult'][0][0]['tgt']

if __name__ == '__main__':
    print(youdao('hello world!', 'auto', 'zh-CN', {}))
