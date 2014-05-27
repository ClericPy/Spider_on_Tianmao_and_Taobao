# -*- coding: utf-8 -*-
import urllib.request
import re
from time import clock as now

'''
测试结果

商品ID、价格、评论数、评分、月销量、总库存:
('39086934885', '85.00', '0', '4.8', '0', '1318')
本次淘宝爬虫执行时间约为： 4.16 s
商品ID、价格、评论数、评分、月销量、总库存:
(36879577205, 'error', '3296', '4.8', '3625', '4454')
本次天猫爬虫执行时间约为： 3.13 s
'''


def gettao(pid):
    pid = str(pid)
    url = r'http://item.taobao.com/item.htm?spm=a217m.7288829.1997547445.4.d2BNzo&id=' + \
        str(pid)
    headers1 = {'GET': '',
                'Host': "item.taobao.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': url}
    req = urllib.request.Request(url, headers=headers1)
    scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    price = re.search(r'<em class="tb-rmb-num">(.*?)</em>', scode).group(1)

    url = r'http://count.tbcdn.cn/counter3?keys=SM_368_sm-357839261,ICE_3_feedcount-%s,SM_368_dsr-357839261&callback=DT.mods.SKU.CountCenter.setReviewCount ' % (
        str(pid))
    req = urllib.request.Request(url, headers=headers1)
    scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    try:
        pinglunshu = re.search(pid + r'":(\d*?),', scode).group(1)
    except:
        pinglunshu = '0'
    pingfen = re.search(r'SM_368_sm-.*?":(.*?),', scode).group(1)
    url = r'http://mdskip.taobao.com/core/initItemDetail.htm?cartEnable=false&callback=setMdskip&itemId=' + \
        str(pid)
    headers1 = {'GET': '',
                'Host': "mdskip.taobao.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': 'http://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.12.UpuePQ&is_b=1&id=' + str(pid)}
    req = urllib.request.Request(url, headers=headers1)
    scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    setcount = re.search(r'sellCount":(.*?)}', scode).group(1)
    kucun = re.search(r'"icTotalQuantity":(.*?),"', scode).group(1)
    # 返回价格、评论数、评分、月销量、总库存
    return (pid, price, pinglunshu, pingfen, setcount, kucun)


def gettian(pid):
    url = r'http://mdskip.taobao.com/core/initItemDetail.htm?cartEnable=false&callback=setMdskip&itemId=' + \
        str(pid)
    headers1 = {'GET': '',
                'Host': "mdskip.taobao.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': 'http://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.12.UpuePQ&is_b=1&id=' + str(pid)}
    req = urllib.request.Request(url, headers=headers1)
    scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    setcount = re.search(r'sellCount":(.*?)}', scode).group(1)
    kucun = re.search(r'"icTotalQuantity":(.*?),"', scode).group(1)
    try:
        url = r'http://item.taobao.com/item.htm?spm=a217m.7288829.1997547445.4.d2BNzo&id=' + \
            str(pid)
        headers1 = {'GET': '',
                    'Host': "item.taobao.com",
                    'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                    'Referer': url}
        req = urllib.request.Request(url, headers=headers1)
        scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
        price = re.search(r'<em class="tb-rmb-num">(.*?)</em>', scode).group(1)
    except:
        url = r'http://mdskip.taobao.com/core/initItemDetail.htm?cartEnable=false&callback=setMdskip&itemId=' + \
            str(pid)
        headers1 = {'GET': '',
                    'Host': "mdskip.taobao.com",
                    'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                    'Referer': 'http://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.12.UpuePQ&is_b=1&id=' + str(pid)}
        req = urllib.request.Request(url, headers=headers1)
        scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
        setcount = re.search(r'sellCount":(.*?)}', scode).group(1)
        try:
            price = re.findall(r'"price":"(\d*\.\d*)","promText', scode)[0]
        except:
            price = 'error'

    url = r'http://dsr.rate.tmall.com/list_dsr_info.htm?itemId=' + str(pid)
    headers1 = {'GET': '',
                'Host': "dsr.rate.tmall.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': 'http://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.8.C2H93V&id=' + str(pid)}
    req = urllib.request.Request(url, headers=headers1)
    scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    pingfen = re.search(r'{"gradeAvg":(.*?),"', scode).group(1)
    pinglunshu = re.search(r'"rateTotal":(.*?)}', scode).group(1)
    return (pid, price, pinglunshu, pingfen, setcount, kucun)


# 测试淘宝 Demo


print('商品ID、价格、评论数、评分、月销量、总库存:')
start = now()
print(gettao(39086934885))
finish = now()
tt = finish - start

print('本次淘宝爬虫执行时间约为：', round(tt, 2), 's')

# 测试天猫
print('商品ID、价格、评论数、评分、月销量、总库存:')
start = now()
print(gettian(36879577205))
finish = now()
tt = finish - start

print('本次天猫爬虫执行时间约为：', round(tt, 2), 's')
