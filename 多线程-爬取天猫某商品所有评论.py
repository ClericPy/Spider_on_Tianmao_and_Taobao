import requests
import json
import re


'''由于该脚本测试过程中不小心弄成600线程同时连接，被封了一小时IP，不过可以挂代理，唉。基本没什么问题了，思路是先获取总评论数，然后每页放20就对20整除，结果加1页就是总页码了。
用到了多线程，完成所需时间大约是1~4s，挂代理速度好的情况下是4~7s
'''


def getmaxrate(pid):
    pid = str(pid)
    # 先获取总评论数
    url = r'http://dsr.rate.tmall.com/list_dsr_info.htm?itemId=' + pid
    r = requests.get(url)
    maxrate = re.search('"rateTotal":(\d+)', r.text).group(1)
    return int(maxrate)


def getrate_tmall(pid, page):
    # proxies1 = {
    #     "http": "61.157.126.37:18000",
    # }
    # headers1 = {'GET': '',
    #             'Host': "dsr.rate.tmall.com",
    #             'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
    #             'Referer': 'http://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.8.C2H93V&id=' + str(pid)}

    url = 'http://rate.tmall.com/list_detail_rate.htm?itemId={}&content=0&currentPage={}'.format(
        pid, page)
    r = requests.get(url)  # , proxies=proxies1, headers=headers1)
    st = r.text
    ss = json.loads('{' + st + '}')
    aa = [i['rateContent']
          for i in ss['rateDetail']['rateList'] if i['rateContent'] != '此用户没有填写评论!']
    global ll
    ll[page] = aa

    return

ll = dict()
pid = '37114811581'

import threading

# for i in range(1, getmaxrate(pid) // 20 + 2):
#     t = threading.Thread(target=getrate_tmall, args=(pid, i,))
#     t.start()
# results = json.dumps(ll, sort_keys=True)

treads = []

for i in range(1, getmaxrate(pid) // 20 + 2):
    treads.append(threading.Thread(target=getrate_tmall, args=(pid, i)))
for t in treads:
    t.start()
for t in treads:
    t.join()
print(ll)
