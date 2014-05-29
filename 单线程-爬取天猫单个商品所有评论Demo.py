import requests
import json

'''
依然是老办法，从json里获取评论，最后依然是存入json文件，与京东那个类似，暂时没时间做多线程了
'''


def getrate_tmall(pid):
    pid = str(pid)
    pagenum = 1
    results = {}
    while 1:
        r = requests.get(
            'http://rate.tmall.com/list_detail_rate.htm?itemId={}&currentPage={}'.format(pid, pagenum))
        aa = r.text[15:]
        ss = json.loads(aa)
        lastpage = ss['paginator']['lastPage']
        contents = [i['rateContent'] for i in ss['rateList']]
        results[pagenum] = contents
        if pagenum != lastpage:
            pagenum += 1
            continue
        else:
            break
    with open('ratetmall_single.json', 'w') as f:
        f.write(
            json.dumps(results, sort_keys=True, indent=4, separators=(',', ': ')))
    print('Finished')
    return 'ok'

# http://detail.tmall.com/item.htm?spm=a230r.1.14.122.IoRmKV&id=37114811581
getrate_tmall(37114811581)
