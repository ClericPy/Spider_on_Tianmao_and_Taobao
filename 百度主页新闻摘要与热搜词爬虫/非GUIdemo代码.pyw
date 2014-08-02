import requests
'''
返回一个元组，每一项是一个列表，列表元素是（标题，URL）组合的元组，所以这两个列表都可以dict()成字典
'''


def baidunews():
    headers = {'Host': 'www.baidu.com', 'Referer': 'http://www.baidu.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0', 'Cookie': 'BDUSS=jU2WjhQSzd2bTZTa0JhdXFYNG9DUzN5ZERqU3NhUU1VZmJlNmF1ZFFCTWFhd1JVQVFBQUFBJCQAAAAAAAAAAAEAAADZhwsBbGlkb25nb25lAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABre3FMa3txTW'}
    r = requests.get(
        'http://www.baidu.com/home/xman/data/newscontent', headers=headers)
    r.encoding = 'base64'
    aa = r.text
    aa = eval(aa)

    hotWords = aa['data']['hotWords']
    hotWords = [(i['key'], 'http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=' + i['key'])
                for i in hotWords]
    imgNews = aa["data"]["imgNews"]
    imgNews = [(i['title'], i['url'].replace('%3A', ':')) for i in imgNews]
    return (imgNews, hotWords)
print(baidunews())
