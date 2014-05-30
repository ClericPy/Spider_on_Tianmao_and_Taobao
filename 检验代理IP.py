import requests
import re
import threading

'''
获得的代理IP来自百度上搜的，关键词：IP代理

'''


def getip(ss):
    aa = re.findall(r'\d+\.\d+\.\d+\.\d+:\d+', ss)
    return aa


def checkip(aa):
    try:
        proxies1 = {"http": aa}
        r = requests.get(
            'http://www.baidu.com', proxies=proxies1, timeout=2)

        if r.status_code == requests.codes.ok:

            print(aa, '   ok')
            aa.append(i)
        else:
            print(aa, '   not ok')
    except:
        pass
    return

ss = '''
1.179.147.2:8080@HTTP#泰国
5.39.68.172:3128@HTTP#法国
5.129.231.10:3128@HTTP#俄罗斯
5.135.98.113:3128@HTTP#法国
5.175.147.245:3128@HTTP#德国
5.223.112.253:8080@HTTP#伊朗
'''
tt = []
for i in getip(ss):
    tt.append(threading.Thread(target=checkip, args=(i,)))
for i in tt:
    i.start()
