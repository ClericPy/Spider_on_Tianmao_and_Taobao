# -*- coding: utf-8 -*-
import urllib.request
import re
from time import clock as now

'''
主要功能是处理一大堆包含商品的网址字符串，然后先从中提取出商品ID，再自动识别天猫或淘宝并进行爬取商品ID、价格、评论数、评分、月销量、总库存，因为是demo，评论内容、商品标题等功能爬取下次再写。demo运行结果为：

商品ID、价格、评论数、评分、月销量、总库存:
('38872202033', '285.00', '0', '5.0', '13', '6')
('38633948046', '388.00', '124', '4.8', '949', '3537')
('19071533066', '58.00', '117', '4.8', '86', '1759')
('38010450966', '519.01', '2', '4.8', '1', '58')
('38069204663', '410.00', '3', '4.8', '1', '392')
本次执行时间约为： 3.55 s    共爬取 5 件商品
'''


def getid(url1):
    aa = re.findall(r'&id=(\d{11})', uu)
    return set(aa)


def gettao(pid):
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
    pinglunshu, pingfen = re.findall(r'":(.*?),"SM_368', scode)
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
    url = r'http://item.taobao.com/item.htm?spm=a217m.7288829.1997547445.4.d2BNzo&id=' + \
        str(pid)
    headers1 = {'GET': '',
                'Host': "item.taobao.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': url}
    req = urllib.request.Request(url, headers=headers1)
    scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    price = re.search(r'<em class="tb-rmb-num">(.*?)</em>', scode).group(1)
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

# 测试一大段字符串里提取id然后获取内容   ↓ ↓ ↓ ↓ ↓ ↓

# uu是测试字符串，可以更改成文本文件中获取的内容
uu = 'http://item.taobao.com/item.htm?spm=a217m.7288829.1997547445.4.d2BNzo&id=38872202033&_scm=1029.list.htm.item.2http://item.taobao.com/item.htm?spm=a217v.7279517.1997511961.2.cFRXBx&id=38633948046&scm=1029.minilist-17.1.50071849&ppath=&sku=&ug=#detailhttp://item.taobao.com/item.htm?spm=a217v.7284005.1997526621.20.wusnZs&id=19071533066&scm=1029.minilist-17.1.50071851&ppath=&sku=&ug=#detailhttp://item.taobao.com/item.htm?spm=a217v.7284193.1997527029.6.pnUSxm&id=38010450966http://item.taobao.com/item.htm?spm=a217v.7284193.1997527029.12.pnUSxm&id=38069204663'


print('商品ID、价格、评论数、评分、月销量、总库存:')
start = now()
for i in getid(uu):
    try:
        print(gettao(i))
    except:
        print(gettian(i))
finish = now()
tt=finish = now()

print('本次执行时间约为：',round(tt,2),'s','\t共爬取',len(getid(uu)),'件商品')