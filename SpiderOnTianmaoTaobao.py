# -*- coding: utf-8 -*-
import urllib.request
import re
from time import clock as now

'''
主要功能是处理一大堆包含商品的网址字符串，然后先从中提取出商品ID，再自动识别天猫或淘宝并进行爬取商品ID、价格、评论数、评分、月销量、总库存，因为是demo，评论内容、商品标题等功能爬取下次再写。注意：getid()函数的正则&aid=(\d{11})根据实际情况，有时候是&id=(\d{11})

demo运行结果为：


商品ID、价格、评论数、评分、月销量、总库存:
('39086994584', '78.00', '0', '4.8', '0', '19997')
('39083055550', '109.00', '0', '4.8', '1', '49')
('39086806561', '99.00', '0', '4.8', '0', '480')
('39107261610', '120.00', '0', '5.0', '2', '795')
('39086946845', '104.99', '0', '5.0', '0', '1998')
('39116476741', '116.00', '0', '4.8', '0', '100')
('39083067634', '50.00', '0', '4.8', '2', '7997')
('39083019686', '39.00', '0', '5.0', '1', '149')
('39086962640', '66.67', '0', '4.8', '0', '10000')
('39116496693', '98.00', '0', '5.0', '0', '6666')
('39116652459', '349.00', '0', '5.0', '0', '1675')
('39107441225', '29.00', '0', '5.0', '20', '39962')
('39116648476', '197.50', '0', '5.0', '0', '399')
('39083127379', '83.00', '0', '4.8', '2', '2992')
('39083087622', '168.00', '0', '4.8', '4', '25335')
('39082835933', '69.90', '0', '4.8', '1', '282')
('39086906766', '119.00', '0', '4.8', '0', '3108')
('39082955012', '159.00', '0', '5.0', '7', '1500')
('39116584727', '50.00', '0', '5.0', '0', '35555')
('39116600547', '125.00', '0', '5.0', '9', '9990')
('39107429215', '75.00', '0', '4.8', '0', '4490')
('39116720284', '38.00', '0', '4.8', '0', '6000')
('39116604665', '168.00', '0', '4.8', '5', '24903')
('39116460805', '158.00', '0', '4.8', '4', '3995')
('39087110367', '374.00', '0', '5.0', '0', '1808')
('39081599183', '128.00', '0', '5.0', '0', '1072')
('39107321380', '308.00', '0', '4.8', '0', '997')
('39082819516', '139.00', '0', '4.8', '7', '387')
('39086926309', '159.00', '0', '5.0', '2', '598')
('39116476411', '99.00', '0', '4.8', '1', '149')
('39083043563', '59.90', '0', '4.8', '0', '23999')
('39082959743', '188.00', '0', '5.0', '6', '9994')
('39116240596', '39.00', '0', '5.0', '0', '43')
('39107217763', '128.00', '0', '4.8', '2', '53161')
('39116316989', '40.00', '0', '4.8', '0', '9999')
('39086862860', '32.00', '0', '5.0', '0', '7999')
('39082863791', '189.00', '0', '5.0', '0', '1877')
('39087034622', '65.00', '0', '5.0', '4', '9994')
('39107201615', '55.00', '0', '4.8', '2', '7997')
('39087242109', '128.00', '0', '5.0', '2', '527')
('39107513088', '96.00', '0', '4.8', '1', '3998')
('39116640422', '128.00', '0', '5.0', '9', '20004')
('39106765471', '128.00', '0', '5.0', '7', '4624')
('39087102144', '99.00', '0', '5.0', '2', '898')
('39116572558', '61.00', '0', '5.0', '0', '24000')
('39116880022', '76.00', '0', '5.0', '3', '10593')
('39107345425', '74.99', '0', '4.8', '0', '7995')
('39116720324', '75.00', '0', '5.0', '0', '350')
('39082839943', '98.00', '0', '5.0', '15', '1482')
('39107517119', '145.00', '0', '4.8', '1', '119982')
('39107177684', '58.00', '0', '5.0', '2', '17996')
('39106733796', '128.00', '0', '4.8', '5', '1134')
('39082943953', '99.99', '0', '5.0', '0', '1999')
('39107333468', '128.00', '0', '5.0', '0', '8000')
('39086934885', '85.00', '0', '5.0', '0', '1318')
('39087030680', '99.00', '0', '5.0', '49', '4950')
('39107237537', '45.00', '0', '4.8', '0', '60000')
('39107437229', '119.00', '0', '4.8', '1', '266442')
('39107377357', '99.00', '0', '5.0', '0', '100')
('39116596703', '35.00', '0', '4.8', '0', '450')
本次执行时间约为： 34.93 s   共爬取 60 件商品

'''


def getid(url1):
    try:
        aa = re.findall(r'&aid=(\d{11})', uu)  #需要根据实际情况来修改，有时候是&id=(\d{11})
    except:
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
uu = '''

    <!DOCTYPE html>
    <html class="ks-gecko29 ks-gecko ks-firefox29 ks-firefox">
        <head></head>
        <body>
            <div class="ks-suggest-container input-drop" style="position: absolute; visibility: hidden; left: 691.5px; top: 87px; width: 370px;"></div>
            <script id="tb-beacon-aplus" src="//a.tbcdn.cn/s/aplus_v2.js" exparams="category=&userid=&aplus&yunid="></script>
            <script></script>
            <!--

             引用全网吊顶 

            -->
            <!--

            TMS:761882

            -->
            <!--

             S GLOBAL HTML 

            -->
            <div id="J_SiteNav" class="site-nav"></div>
            <!--

             

            -->
            <!--

             全网顶通 

            -->
            <!--

             E GLOBAL HTML 

            -->
            <script></script>
            <!--

             导航 

            -->
            <!--

            TMS:1095233

            -->
            <link href="http://a.tbcdn.cn/tmse/15/dpl/??sm-nav-2014/v37/sm-nav-2014.css" rel="stylesheet"></link>
            <link href="http://a.tbcdn.cn/tmse/15/dpl/??5611/sm-nav-2014/sm-nav-2014/v37/skin/default.css" rel="stylesheet"></link>
            <div id="guid-1399355373321" class="skin-default" data-type="3" data-version="37" data-guid="1399355373321" data-skin="default" data-name="sm-nav-2014"></div>
            <script src="http://a.tbcdn.cn/tmse/15/dpl/??sm-nav-2014/v37/sm-nav-2014.js"></script>
            <script></script>
            <!--

             POWERED BY DPL 

            -->
            <div id="page">
                <div id="content">
                    <div class="J_Layout layout grid-m0"></div>
                    <div class="J_Layout layout grid-m0s24"></div>
                    <div class="J_Layout layout grid-m0">
                        <div class="col-main">
                            <div class="main-wrap J_Region">
                                <div id="guid-14000559304400" class="J_Module skin-default" data-type="3" data-version="3" data-guid="14000559304400" data-skin="default" data-name="sm-margin"></div>
                                <div id="guid-14000559123800" class="J_Module skin-default" data-type="3" data-version="17" data-guid="14000559123800" data-skin="default" data-name="sm-minilist">
                                    <div class="module" data-spm="1997577493" data-spm-max-idx="180">
                                        <div class="tb-module sm-minilist tb-lazyload app-minilist" data-global-config="{"version":"0.1.6"}" data-config="{"tmsGlobalMiniListUrl":"http:\/\/list.taobao.com\/itemlist\…et=utf-8&user_type=0&at=12034","tmsGlobalMiniListStyle":"0"}">
                                            <div class="app-minilist-inner">
                                                <div id="minilist-filterForm-1"></div>
                                                <div id="minilist-itemList-1">
                                                    <div class="m-itemList">
                                                        <div class="grid">
                                                            <ul class="items clearfix">
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39083127379&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116640422&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116240596&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39083019686&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39107441225&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116880022&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39083055550&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39082819516&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39087030680&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39107517119&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39082955012&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39086926309&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39107177684&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39083087622&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39082835933&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116720324&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39086994584&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116476741&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39106733796&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39087102144&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39106765471&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116652459&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116476411&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116496693&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39082839943&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39107321380&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116460805&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39107261610&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39082959743&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39087242109&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39083043563&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39087110367&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39107333468&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39087034622&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116572558&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116648476&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39107377357&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116316989&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39107217763&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116604665&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39107201615&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39081599183&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39107429215&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116600547&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39107437229&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39086934885&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39107513088&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116596703&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39086906766&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39107345425&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39086946845&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39082863791&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39082943953&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39107237537&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116720284&srow=">
                                                                    <dl class="clearfix"></dl>
                                                                </li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39086806561&srow=">
                                                                    <dl class="clearfix"></dl>
                                                                </li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39086962640&srow=">
                                                                    <dl class="clearfix"></dl>
                                                                </li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39116584727&srow="></li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39086862860&srow=">
                                                                    <dl class="clearfix">
                                                                        <dd class="img"></dd>
                                                                        <dd class="price"></dd>
                                                                        <dt class="title">
                                                                            <a class="J_ItemLink" target="_blank" href="http://item.taobao.com/item.htm?spm=a217f.7295005.1997577493…39086862860&scm=1029.minilist-17.1.16&ppath=&sku=&ug=#detail" data-spm-anchor-id="a217f.7295005.1997577493.176"></a>
                                                                        </dt>
                                                                        <dd class="desc"></dd>
                                                                        <dd class="shopname">
                                                                            <a target="_blank" href="http://store.taobao.com/shop/view_shop.htm?spm=a217f.7295005.1997577493.177.cmuMNX&user_number_id=83014570&ssid=r11" data-spm-anchor-id="a217f.7295005.1997577493.177"></a>
                                                                        </dd>
                                                                        <dd class="location"></dd>
                                                                    </dl>
                                                                </li>
                                                                <li class="item " data-itemloggokey="q=%B4%F2%B5%D7%C9%C0&olu=yes&prepay=1&se=&ss=&st=&sf=&new=2&…&pscm=1029.minilist-17.1.16&src=normal&aid=39083067634&srow="></li>
                                                            </ul>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div id="minilist-page-1">
                                                    <div class="m-page">
                                                        <div class="wraper">
                                                            <div class="inner clearfix">
                                                                <ul class="items"></ul>
                                                                <div class="total"></div>
                                                                <div class="form">
                                                                    <span class="text"></span>
                                                                    <input class="input" type="number" max="100" min="1" value="1"></input>
                                                                    <span class="text"></span>
                                                                    <span class="btn" tabindex="0"></span>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="g_foot">
                <div class="g_foot-ali">
                    <a href="//page.1688.com/shtml/about/ali_group1.shtml "></a>
                    <b></b>
                    <a href="//www.alibaba.com"></a>
                    <b></b>
                    <a href="//www.1688.com"></a>
                    <b></b>
                    <a href="//www.aliexpress.com"></a>
                    <b></b>
                    <a href="//www.taobao.com/index_global.php"></a>
                    <b></b>
                    <a href="//www.tmall.com"></a>
                    <b></b>
                    <a href="//ju.taobao.com"></a>
                    <b></b>
                    <a href="//www.etao.com"></a>
                    <b></b>
                    <a href="//www.alimama.com"></a>
                    <b></b>
                    <a href="//www.aliyun.com"></a>
                    <b></b>
                    <a href="//www.yunos.com"></a>
                    <b></b>
                    <a href="//www.net.cn"></a>
                    <b></b>
                    <a href="//www.alipay.com"></a>
                    <b></b>
                    <a href="//www.laiwang.com"></a>
                </div>
                <div class="g_foot-nav"></div>
                <span class="g_foot-toy"></span>
                <span class="g_foot-line"></span>
            </div>
            <style></style>
            <script src="http://a.tbcdn.cn/tmse/15/dpl/??sm-margin/v3/sm-margin.js,sm-rgn/v1/sm-rgn.js,sm-minilist/v17/sm-minilist.js"></script>
            <script></script>
            <div id="J_Feedback" class="feedback" style="right: 10px;"></div>
            <div id="J_miniCartPlugin" class="mini-cart-plugin"></div>
            <div id="J_UmppUserContainer" style="height:1px;width:1px;overflow:hidden;position:absolute;bottom:1px"></div>
            <iframe style="display: none;" src="http://www.tmall.com/go/act/stp-tm.php?__ga_xd_token=1400567583267TuIPVDD2"></iframe>
            <iframe id="J_Um_Iframe" width="1" height="1" frameborder="0" src="http://mpp.taobao.com/ajaxconn2.html?appId=1064&domain=taobao.org" scrolling="no" style="position: absolute;"></iframe>
        </body>
    </html>

'''


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