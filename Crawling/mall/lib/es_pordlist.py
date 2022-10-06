# -*- coding: utf-8 -*-
from typing import List, Any

from Crawling.common.lib_es import LibES
from elasticsearch import helpers
from Crawling.mall.lib.data_prodlist import DataMallProdlist

class DataMallProdlistES(LibES):
    def __init__(self):
        super(DataMallProdlistES, self).__init__()
        self.indexname = 'mall_prodlist'

    # insert bulk
    def insertProdlistES(self, onedat):
        newDoc = []
        for linedat in onedat:
            onedoc = linedat.get_data_dict()
            # print('onedoc : ', onedoc)

            doc = {'_index': self.indexname, '_source': onedoc}
            # print(doc)
            newDoc.append(doc)
        helpers.bulk(self.es, newDoc, index=self.indexname)

    # search all prodlist
    def getAllProdlist(self):
        try:
            body = {"query":{"match_all": {}},
                    "sort": {
                        "@timestamp": {"order": "DESC"}
                    }}
            res = self.es.search(index=self.indexname, body=body, size=10000)
            return res
        except Exception as ex:
            print('es_oasis_prod - getAllProdlist :', ex)

    # search : mall_code
    def search_mall_code(self, dat, sta):
        body = {
                  "query": {
                    "bool": {
                      "must": [
                        { "match": { "code_mall": dat }},
                        { "match": { "prod_sta": sta }}
                      ]
                    }
                  }
                }
        res = self.es.search(index=self.indexname, body=body, size=10000)
        return res

    ####################
    # Result
    ####################
    def result_all_data(self, res):
        all_data_model = []
        for item in res['hits']['hits']:
            # class
            prod_list = DataMallProdlist()
            prod_list.timestamp = item['_source']['@timestamp']
            prod_list.code_mall = item['_source']['code_mall']
            prod_list.name_mall = item['_source']['name_mall']
            prod_list.name_code_mall = item['_source']['name_code_mall']
            prod_list.prod_category = item['_source']['prod_category']
            prod_list.prod_category_name = item['_source']['prod_category_name']
            prod_list.prodlist_url = item['_source']['prodlist_url']

            prod_list.code_prod_hit = item['_source']['code_prod_hit']
            prod_list.code_prod_origin = item['_source']['code_prod_origin']
            prod_list.prod_name = item['_source']['prod_name']
            prod_list.prod_price = item['_source']['prod_price']
            prod_list.prod_sta = item['_source']['prod_sta']

            prod_list.in_date = item['_source']['in_date']
            prod_list.main_image = item['_source']['main_image']
            prod_list.detail_url = item['_source']['detail_url']
            prod_list.prod_unit = item['_source']['prod_unit']

            # data class set dict
            prod_list.set_data_dict()
            all_data_model.append(prod_list)
        return all_data_model

    # def result_all_name(self, item):


    def result_one_data(self, item):
        # class
        prod_list = DataMallProdlist()
        prod_list.timestamp = item['_source']['@timestamp']
        prod_list.code_mall = item['_source']['code_mall']
        prod_list.name_mall = item['_source']['name_mall']
        prod_list.name_code_mall = item['_source']['name_code_mall']
        prod_list.prod_category = item['_source']['prod_category']
        prod_list.prod_category_name = item['_source']['prod_category_name']
        prod_list.prodlist_url = item['_source']['prodlist_url']

        prod_list.code_prod_hit = item['_source']['code_prod_hit']
        prod_list.code_prod_origin = item['_source']['code_prod_origin']
        prod_list.prod_name = item['_source']['prod_name']
        prod_list.prod_price = item['_source']['prod_price']
        prod_list.prod_sta = item['_source']['prod_sta']

        prod_list.in_date = item['_source']['in_date']
        prod_list.main_image = item['_source']['main_image']
        prod_list.detail_url = item['_source']['detail_url']
        prod_list.prod_unit = item['_source']['prod_unit']

        # data class set dict
        prod_list.set_data_dict()
        return prod_list


