import requests

''''
自动爬取某单个商品的所有评论内容，速度因为使用多线程，大约1秒就按页码顺序存入ratejd.json，解析查看可以运行“解析json.py”。

注意：这里使用了一个requests模块，需要去第三方下载，可以通过pip
pip install requests
'''

# ll是用来存放评论内容列表的，key是页码，value是存放10个当页评论的列表

ll = {}

pid = '967821'
headers1 = {'GET': '',
            'Host': "club.jd.com",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
            'Referer': 'http://item.jd.com/{}.html'.format(pid)}

r1 = requests.get(
    'http://club.jd.com/productpage/p-{}-s-0-t-3-p-{}.html'.format(pid, 0), headers=headers1)

maxpagenum = r1.json()['productCommentSummary'][
    'commentCount'] // 10  # 先获取最大页码数


def getrate_jd(pagenum):
    global pid  # 这里用全局是因为写这个脚本的时候对map不太熟练，其实多参数可以用元组的
    '''该函数用来获取商品ID是pid的第pagenum页的评论列表'''
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


from multiprocessing.dummy import Pool

pool = Pool(10)  # 10线程192条评论用了5秒，测试线程池15和4差距2秒，还好京东不封IP，差距不大可能因为网速
urls = list(range(maxpagenum + 1))
results = pool.map(getrate_jd, urls)
pool.close()
pool.join()
print(ll)
