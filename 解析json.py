# -*- coding: utf-8 -*-
import json


def main():
    with open('ratejd.json') as f:
        aa = json.load(f)
    print(aa)
    with open('ratetmall_single.json') as f:
        aa = json.load(f)
    print(aa)


if __name__ == '__main__':
    main()
