import requests

''''
自动爬取某单个商品的所有评论内容，速度有待优化，暂时不做多线程处理。
Demo代码如下。
注意：这里仅使用了一个requests模块，需要去第三方下载，可以通过pip
pip install requests

'''

pid = '967821'
headers1 = {'GET': '',
            'Host': "club.jd.com",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
            'Referer': 'http://item.jd.com/{}.html'.format(pid)}


pagenum = 0
while 1:
    r = requests.get(
        'http://club.jd.com/productpage/p-{}-s-0-t-3-p-{}.html'.format(pid, pagenum), headers=headers1)
    aa = r.json()
    ss = [x['content'] for x in aa['comments']]
    if ss != []:
        print('=========================评论第 ',
              pagenum, ' 页=========================')
        print(*ss)
        pagenum += 1
    else:
        break

print('\n\n\n评论爬虫结束，共爬取{}页评论'.format(pagenum))
