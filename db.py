# -*- coding: utf-8 -*-
import pymongo

MONGO_DB = 'biying'
MONGO_COLLECTION = 'biying_img'


class Mongo(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.client[MONGO_DB]

    def add(self, data):
        """
        添加数据到数据库
        :param data:
        :return:
        """
        if data:
            self.db[MONGO_COLLECTION].insert(data)
            print('保存到{}成功'.format(data))
