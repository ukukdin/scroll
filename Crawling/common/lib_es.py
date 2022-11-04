# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
# import data.onch_info as Info
from elasticsearch import helpers



class LibES:
    def __init__(self):
        # self.man = Info.searchmaxcount
        self.man = 10000
        self.esip = '192.168.0.43:9200'
        # self.esip = '127.0.0.1:9200'
        self.es = Elasticsearch(self.esip)


    def getConnection(self):
        return self.es

    def closeConnectES(self):
        self.es.transport.close()


    def deleteIndex(self, indexName):
        self.es.indices.delete(index=indexName, ignore=[400, 404])

    def get_all_index_name(self):
        all_index = []
        tmp_index = self.es.indices.get('*')

        for in_index in tmp_index:
            all_index.append(in_index)
        return all_index

    def is_index(self, index_name):
        all_idex = self.get_all_index_name()
        # print(type(all_idex))

        # print('index_name : ', index_name)
        is_key = False

        # print(all_idex)
        if index_name in all_idex:
            is_key = True
            # print('in')
        return is_key

    ####################
    # Count
    ####################
    def get_index_count(self, indexname):
        try:
            result = self.es.count(index=indexname, body=None)
        except Exception:
            raise AssertionError("Count Error : ", indexname)
        return result['count']

    ####################
    # insert
    ####################
    # insert 한 건씩
    def insert_data(self, cls, indexname):
        try:
            docu = cls.get_data_dict()
            res = self.es.index(index=indexname, body=docu)
            return res
        except Exception as ex:
            print('Error : ', ex)

    # def insert_data_id(self, cls, indexname):
    #     try:
    #         docu = cls.get_data_dict()
    #         sellerProductItemId = cls['sellerProductItemId']
    #         res = self.es.index(index=indexname, id=sellerProductItemId, body=cls)
    #     except Exception as ex:
    #         print('Error : ', ex)

    # insert bulk
    def insert_bulk_es(self, onedat, indexname):
        newDoc = []
        for linedat in onedat:
            onedoc = linedat.get_data_dict()

            doc = {'_index': indexname, '_source': onedoc}
            # print(doc)
            newDoc.append(doc)
        helpers.bulk(self.es, newDoc, index=indexname)

    ####################
    # search
    ####################
    # search all prodlist
    def get_all_data(self, indexname):
        try:
            body = {"query":{"match_all": {}},
                    "sort": {
                        "@timestamp": {"order": "DESC"}
                    }}
            res = self.es.search(index=indexname, body=body, size=10000)
            return res
        except Exception as ex:
            print('Libes - get_all_data :', ex)


if __name__ == '__main__':
    config = 'create'
    if config == 'create':

        es = LibES()
        # es.createIndex('onchctg_test')

        indexname = "onch_new_prodhtml_2021-10-23"
        es.get_all_index_name()
        # es.healthCheck()
        # es.closeConnectES()