from qtui import Ui_Form
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QInputDialog
import sys
import requests
import re
from lxml import _elementpath


class myqt(QtWidgets.QWidget, Ui_Form):

    """docstring for myqt"""

    def __init__(self):
        super(myqt, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start)
        self.lineEdit.setText('967821')
        self.pushButton.clicked.connect(
            lambda: self.pushButton_2.setEnabled(True))
        self.pushButton_2.clicked.connect(self.saveasjson)

    def saveasjson(self):
        import json
        cc = dict(enumerate(bb))
        with open('{}.json'.format(pid), 'w') as f:
            ee = json.dump(cc, f)

    def start(self):
        self.listWidget.clear()
        self.textEdit.clear()
        global pid
        pid = self.lineEdit.text()
        pid = re.findall('(\d{3,})', pid)[0]
        _ = requests.get('http://item.jd.com/{}.html'.format(pid))
        _.encoding = 'gb2312'
        ptitle = re.search('<h1>(.*?)</h1>', _.text).group(1).replace('\n', '')
        self.label_3.setText("商品名称：{}".format(ptitle))
        global bb
        bb = crawl(pid)
        cc = maxpagenum(pid)
        for i in range(cc + 1):
            self.listWidget.addItem(str(i))
        self.listWidget.itemClicked.connect(self.bindll)

    def bindll(self, item):
        ee = '\n\n'.join(bb[int(item.text())])
        self.textEdit.setText(ee)


def maxpagenum(pid):
    headers1 = {'GET': '',
                'Host': "club.jd.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': 'http://item.jd.com/{}.html'.format(pid)}

    r1 = requests.get(
        'http://club.jd.com/productpage/p-{}-s-0-t-3-p-{}.html'.format(pid, 0), headers=headers1)
    # 先获取最大页码数
    ss = r1.json()['productCommentSummary']['commentCount'] // 10
    return ss

# print(maxpagenum)


def getrate_jd(pp):
    pid = pp[0]
    pagenum = pp[1]
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
        return ss


def crawl(pid):
    from multiprocessing.dummy import Pool
    urls = []

    pool = Pool(50)
    for i in range(maxpagenum(pid) + 1):
        urls.append((pid, i))
    results = pool.map(getrate_jd, urls)
    pool.close()
    pool.join()
    return results

app = QtWidgets.QApplication(sys.argv)
aa = myqt()
aa.show()
sys.exit(app.exec_())
