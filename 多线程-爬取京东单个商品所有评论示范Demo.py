import requests

''''
自动爬取某单个商品的所有评论内容，速度因为使用多线程，大约1秒就按页码顺序存入ratejd.json，解析查看可以运行“解析json.py”。

注意：这里使用了一个requests模块，需要去第三方下载，可以通过pip
pip install requests
'''
ll = {}
pid = '967821'
headers1 = {'GET': '',
            'Host': "club.jd.com",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
            'Referer': 'http://item.jd.com/{}.html'.format(pid)}

r1 = requests.get(
    'http://club.jd.com/productpage/p-{}-s-0-t-3-p-{}.html'.format(pid, 0), headers=headers1)
maxpagenum = r1.json()['productCommentSummary']['commentCount'] // 10

# print(maxpagenum)


def getrate_jd(pid, pagenum):
    headers1 = {'GET': '',
                'Host': "club.jd.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': 'http://item.jd.com/{}.html'.format(pid)}
    r = requests.get(
        'http://club.jd.com/productpage/p-{}-s-0-t-3-p-{}.html'.format(pid, pagenum), headers=headers1)
    aa = r.json()
    ss = [x['content'] for x in aa['comments']]
    global ll
    if ss != []:
        ll[pagenum] = ss


import threading
treads = []

for i in range(maxpagenum + 1):
    treads.append(threading.Thread(target=getrate_jd, args=(pid, i)))
for t in treads:
    t.start()

import json

with open('ratejd.json', 'w') as f:
    f.write(json.dumps(ll, sort_keys=True, indent=4, separators=(',', ': ')))
