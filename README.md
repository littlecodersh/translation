# translation

![python27](https://img.shields.io/badge/python-2.7-ff69b4.svg) ![python35](https://img.shields.io/badge/python-3.5-green.svg) [English version](https://github.com/littlecodersh/translation/blob/master/README_EN.md)

translation是一个基于网页端翻译的python翻译包。

提供基本的谷歌、有道、百度、金山翻译服务。

目前提供的谷歌的翻译服务暂时不需要使用代理。

## Installation

```bash
pip install translation
```

## Usage

```python
from translation import baidu, google, youdao, iciba, bing

print(google('hello world!', dst = 'zh-CN'))
print(google('hello world!', dst = 'ru'))
print(baidu('hello world!', dst = 'zh'))
print(baidu('hello world!', dst = 'ru'))
print(youdao('hello world!', dst = 'zh-CN'))
print(iciba('hello world!', dst = 'zh'))
print(bing('hello world!', dst = 'zh-CHS'))
```

## Documents

你可以在[这里](http://translation.readthedocs.io/zh_CN/latest/)获取api的使用帮助。

## Advanced usage

### Proxies

你可能无法在国内使用谷歌或者在国外使用有道和金山的翻译。

这是你可以尝试使用代理。

```python
from translation import google, ConnectError

# 127.0.0.1:1080 is a vaild proxies
try:
    print(google('hello world!', dst = 'zh-CN', proxies = {'http': '127.0.0.1:1080'}))
except ConnectError:
    print('Invaild proxy')
```

### Default

你可以更改默认的设置，可更改的设置包括：
* 默认的源语言（不修改则会自动识别）
* 默认的目标语言（不修改则为中文）
* 默认的首选翻译（不修改则为有道）
* 默认的代理（不修改则为不使用代理）

```python
from translation import (set_default_translation, set_default_language,
    set_default_proxies, get, ConnectError)

set_default_translation('google')
set_default_language('auto', 'zh-CN')
set_default_proxies({'http': '127.0.0.1:1080'})
try:
    print(get('hello world!'))
except ConnectError:
    print('Invaild proxy')
```

### More

更多的功能可以参考[文档](http://translation.readthedocs.io/zh_CN/latest/)。

## Language

[文档](http://translation.readthedocs.io/zh_CN/latest/)中有详细的支持语言的列表，这里仅给出谷歌支持语言的标记列表。

其中金山词霸，有道翻译仅支持文档给出的语言翻译为中文。

**Google**
```
el    : Greek,
eo    : Esperanto,
en    : English,
af    : Afrikaans,
sw    : Swahili,
ca    : Catalan,
it    : Italian,
iw    : Hebrew,
sv    : Swedish,
cs    : Czech,
cy    : Welsh,
ar    : Arabic,
ur    : Urdu,
ga    : Irish,
eu    : Basque,
et    : Estonian,
az    : Azerbaijani,
id    : Indonesian,
es    : Spanish,
ru    : Russian,
gl    : Galician,
nl    : Dutch,
pt    : Portuguese,
la    : Latin,
tr    : Turkish,
tl    : Filipino,
lv    : Latvian,
lt    : Lithuanian,
th    : Thai,
vi    : Vietnamese,
gu    : Gujarati,
ro    : Romanian,
is    : Icelandic,
pl    : Polish,
ta    : Tamil,
yi    : Yiddish,
be    : Belarusian,
fr    : French,
bg    : Bulgarian,
uk    : Ukrainian,
hr    : Croatian,
bn    : Bengali,
sl    : Slovenian,
ht    : Haitian Creole,
da    : Danish,
fa    : Persian,
hi    : Hindi,
fi    : Finnish,
hu    : Hungarian,
ja    : Japanese,
ka    : Georgian,
te    : Telugu,
zh-TW : Chinese Traditional,
sq    : Albanian,
no    : Norwegian,
ko    : Korean,
kn    : Kannada,
mk    : Macedonian,
zh-CN : Chinese Simplified,
sk    : Slovak,
mt    : Maltese,
de    : German,
ms    : Malay,
sr    : Serbian
```

## Comments

如果有什么问题或者建议都可以在这个[Issue](https://github.com/littlecodersh/translation/issues/1)和我讨论。
