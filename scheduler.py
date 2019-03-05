# -*- coding: utf-8 -*-
import time
import datetime
from crawler import Crawler
from db import Mongo


class Scheduler(object):
    def __init__(self):
        self.crawler = Crawler()
        self.db = Mongo()

    def run(self, url, date):
        """
        开始爬取并保存
        :param url: 爬取url
        :param date: 爬取时间
        :return:
        """
        data = self.crawler.main(url)
        data['date'] = date
        self.db.add(data)

    def main(self, url, h=1, m=0):
        """
        主程序入口
        :param url: 爬取url
        :param h: 执行程序的时间
        :param m:执行程序的时间
        :return:
        """
        while True:
            now = datetime.datetime.now()
            date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
            if now.hour == h and now.minute == m:
                self.run(url, date)
            # 每个60秒检测一次
            time.sleep(60)


if __name__ == '__main__':
    sch = Scheduler()
    sch.main('https://cn.bing.com')
