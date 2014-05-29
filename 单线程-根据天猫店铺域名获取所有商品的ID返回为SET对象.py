import requests
import json
import lxml.html
import re

'''
考虑到去重，返回值用的是集合，考虑到页码不会太多，所以暂时不用多线程了，又考虑到信息量不大，所以不输出成文件了，直接打印出来了，返回值可以做的东西很多，比如调用多线程来进行另外两个模块对天猫所有评价内容的爬取以及价格销量等信息的获取。其他爬虫以后再说吧
'''


def getids_tmall(shopname):
    # 先初始化获取最大页码和第一页的ID列表
    url = 'http://{}.tmall.com/search.htm?spm=&pageNo=1'.format(shopname)
    r = requests.get(url)
    scode = r.text
    doc = lxml.html.document_fromstring(scode)
    ss = doc.xpath('//p/b[@class="ui-page-s-len"]/text()')
    hrefs = doc.xpath(
        '//div[@class = "J_TItems"] // a[@class = "item-name"] / @href')
    h1 = re.findall(r'id=(\d{11})', str(hrefs))
    maxpagenum = ss[0].replace('1/', '')
    # 对剩余每页获取ID列表
    if maxpagenum == 1:
        return set(h1)
    else:
        for i in range(2, int(maxpagenum) + 1):
            url = 'http://{}.tmall.com/search.htm?spm=&pageNo={}'.format(
                shopname, i)
            r = requests.get(url)
            scode = r.text
            doc = lxml.html.document_fromstring(scode)
            hrefs = doc.xpath(
                '//div[@class = "J_TItems"] // a[@class = "item-name"] / @href')
            h1 += re.findall(r'id=(\d{11})', str(hrefs))
        return set(h1)

# http://chipisheaumeiu.tmall.com/index.htm?spm=a1z10.3.w5002-3029434437.2.CUFVDk例子中截取（也可以自动截取，正则很容易）商铺域名中的‘chipisheaumeiu’部分作为参数传入即可

print(getids_tmall('chipisheaumeiu'))
