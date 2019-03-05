# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq


class Crawler(object):
    def get_page_html(self, url):
        """
        获取网页源码
        :param url:
        :return:
        """
        if url:
            response = requests.get(url)
            print('正在爬取{}，状态码为{}'.format(url, response.status_code))
            if response.status_code == 200:
                return response.text
        return None

    def parse(self,page_url, html):
        """
        解析页面
        :param html:
        :return:
        """
        if html:
            doc = pq(html)
            url = doc('#bgLink').attr('href')
            url_info = doc('#sh_cp').attr('title')
            data = {
                'url': page_url + url,
                'url_info': url_info
            }
            print(data)
            return data

    def main(self, url):
        """
        爬虫入口
        :param url:
        :return:
        """
        html = self.get_page_html(url)
        return self.parse(url,html)
