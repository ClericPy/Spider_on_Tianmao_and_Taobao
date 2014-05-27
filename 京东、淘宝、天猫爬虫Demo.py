# -*- coding: utf-8 -*-
import urllib.request
import re
from time import clock as now
import json

'''
====================测试结果=======================

商品ID 价格(原价) 1星 2星 3星 4星 5星 评论数 平均评分 好评数 好评率 中评数 中评率 差评数 差评率 :
967821 3199.00(3800.00) 19 7 35 175 556 792 5 731 0.924 42 0.053 19 0.023
本次京东爬虫执行时间约为： 0.48 s

商品ID、价格、评论数、评分、月销量、总库存:
39086934885 85.00 0 4.6 3 1315
本次淘宝爬虫执行时间约为： 1.13 s

商品ID、价格、评论数、评分、月销量、总库存:
36879577205 null 3730 4.8 3911 4309
本次天猫爬虫执行时间约为： 10.32 s

'''


def getjd(pid):
    '''通过京东服务器查'''
    pid = str(pid)
    # 上面获取了商品ID，下面就是把ID添加到京东那个查价格的json地址里
    url = 'http://p.3.cn/prices/get?skuid=J_' + str(pid)
    html = urllib.request.urlopen(url).read().decode('utf-8')
    nprice = re.search(r'"p":"(.*?)"', html).group(1)
    oprice = re.search(r'"m":"(.*?)"}', html).group(1)
    price = nprice + '(' + oprice + ')'
    url = r'http://club.jd.com/productpage/p-{}-s-0-t-3-p-0.html'.format(
        pid)
    headers1 = {'GET': '',
                'Host': "club.jd.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': 'http://item.jd.com/%s.html' % (pid)}
    req = urllib.request.Request(url, headers=headers1)
    scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    dd = json.loads(scode)
    # print('1星', '2星', '3星', '4星', '5星', '评论数',
    #       '平均评分', '好评数', '好评率', '中评数', '中评率', '差评数', '差评率 :')
    return (pid, price, dd['productCommentSummary']['score1Count'], dd['productCommentSummary']['score2Count'], dd['productCommentSummary']
            ['score3Count'], dd['productCommentSummary']['score4Count'], dd['productCommentSummary']['score5Count'], dd['productCommentSummary']['commentCount'], dd['productCommentSummary']['averageScore'], dd['productCommentSummary']['goodCount'], dd['productCommentSummary']['goodRate'], dd['productCommentSummary']['generalCount'], dd['productCommentSummary']['generalRate'], dd['productCommentSummary']['poorCount'], dd['productCommentSummary']['poorRate'])


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
            price = 'null'

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


# 测试京东

print('商品ID', '价格(原价)', '1星', '2星', '3星', '4星', '5星', '评论数',
      '平均评分', '好评数', '好评率', '中评数', '中评率', '差评数', '差评率 :')
start = now()
print(*getjd(967821))
finish = now()
tt = finish - start

print('本次京东爬虫执行时间约为：', round(tt, 2), 's\n')

# 测试淘宝 Demo

print('商品ID、价格、评论数、评分、月销量、总库存:')
start = now()
print(*gettao(39086934885))
finish = now()
tt = finish - start

print('本次淘宝爬虫执行时间约为：', round(tt, 2), 's\n')

# 测试天猫
print('商品ID、价格、评论数、评分、月销量、总库存:')
start = now()
print(*gettian(36879577205))
finish = now()
tt = finish - start

print('本次天猫爬虫执行时间约为：', round(tt, 2), 's\n')
