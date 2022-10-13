from elasticsearch import Elasticsearch
from elasticsearch_dsl import Document, Integer, Keyword, connections,Text,Date
from elasticsearch import helpers
import Crawling.common.util_common as cu
from Zentrade import New_prod,OutofStock
from Zentrade import WholePage
from Zentrade.libara.zen_data import DataZenProduct

import json

class DataMallProdList(Document):
    def __init__(self):
        super(DataMallProdList, self).__init__()
        # 전체페이지
        self.w= WholePage.Whole_list()

        # 전체페이지에서 값
        self.no = self.w.parser_wholelist()
        # 신상품 페이지
        self.n = New_prod.New_List()
        #신상품 페이지 값
        self.np =self.n.NP()
        # 품절 페이지
        self.o = OutofStock.out_of_stock()
        # 품절 페이지값
        self.op =self.o.outstock()
        # # 상세상품 페이지
        # self.p = ProductList.Product_List()
        # # 상세상품 페이지값
        # self.pl = self.p.parser_wholelist()
        self.es = Elasticsearch('[192.168.0.41]:9200')


    # 하나만 실행
    def insertone(self):
        index = 'wholepage'
        doc={
            "prod_num":"num",
            "prod_name":"",
            "prod_price":120333,
            "@timestamp":cu.getDateToday()
        }
        self.es.index(index=index,doc_type="_doc",body=doc)
    # 벌크 넣고 실행
    def insertbulk_whole(self):
        docs = []
        index = 'wholepage'
        for a in self.no:
            self.Wname = a[:][1].string
            self.Wnum = a[:][0]
            self.Wprice=a[:][2].replace(",","")
            docs.append({
               '_index':'wholepage',
                '_source':{
                   'name_mall': self.w.name_mall,
                   'name_code_mall': self.w.name_code_mall,
                   'code_mall':self.w.code_mall,
                   'prod_num':self.Wnum,
                   'prod_name':self.Wname,
                   'prod_price':self.Wprice,
                   '@timestamp':cu.getDateToday()
                    }
            })
        helpers.bulk(self.es,docs,index=index)


    def insertbulk_newprod(self):
        newDoc=[]
        index = 'newprod'

        for b in self.np:
            new_name = b[1]
            new_num = b[0]
            new_date = b[3]
            new_price = b[2].replace(",", "")
            newDoc.append({
                '_index':'newprod',
                '_source':{
                'name_mall': self.n.name_mall,
                 'name_code_mall': self.n.name_code_mall,
                'code_mall': self.n.code_mall,
                'new_prod_num':new_num,
                'new_prod_name':new_name,
                'new_prod_price':new_price,
                'new_prod_date':new_date,
                '@timestamp':cu.getDateToday()
                }
            })
        helpers.bulk(self.es,newDoc,index=index)



    # 전체 가져오기
    def getAllProdlist(self):
        index = 'wholepage'
        try:
            body ={"query":
                       {'match_all':{self.Wnum}}

                   }
            res=self.es.search(index=index,body=body,size=10000)
            return res
        except Exception as ex:
            print("zentrade_whole_list: ",ex)
    # 넙버 값으로 원하는 값 찾기
    def search_prod_num(self):
        index = 'wholepage'
        body ={
                "query":{
                  "bool":{
                    "must":[
                      {"match":{"prod_name":'시스맥스'}}
                        ]
                }
            }
        }

        res = self.es.search(index=index,body=body,size=10000)
        return res

    def result_all_data(self, res):
        all_data_model = []
        for item in res['hits']['hits']:
            # class
            prod_list = DataZenProduct()
            prod_list.timestamp = item['_source']['@timestamp']
            prod_list.code_mall = item['_source']['code_mall']
            prod_list.name_mall = item['_source']['name_mall']
            prod_list.name_code_mall = item['_source']['name_code_mall']
            # prod_list.mall_category = item['_source']['mall_category']
            prod_list.prod_num = item['_source']['prod_num']
            prod_list.prod_name = item['_source']['prod_name']

            prod_list.prod_price = item['_source']['prod_price']
            # prod_list.prod_out = item['_source']['prod_out']
            # prod_list.reason = item['_source']['reason']
            # prod_list.reorder = item['_source']['reorder']
            # prod_list.reorder_date = item['_source']['reorder_date']
            #
            # prod_list.expire_date = item['_source']['expire_date']

            # data class set dict
            prod_list.set_date_dict()
            all_data_model.append(prod_list)
        print(all_data_model)
        return all_data_model

    # def result_all_name(self, item):

    def result_one_data1(self, item):
            # class
            prod_list = DataZenProduct()
            prod_list.timestamp = item['_source']['@timestamp']
            prod_list.code_mall = item['_source']['code_mall']
            prod_list.name_mall = item['_source']['name_mall']
            prod_list.name_code_mall = item['_source']['name_code_mall']
            prod_list.mall_category = item['_source']['mall_category']
            prod_list.prod_num = item['_source']['prod_num']
            prod_list.prod_name = item['_source']['prod_name']

            prod_list.prod_price = item['_source']['prod_price']
            prod_list.prod_out = item['_source']['prod_out']
            prod_list.reason = item['_source']['reason']
            prod_list.reorder = item['_source']['reorder']
            prod_list.reorder_date = item['_source']['reorder_date']

            prod_list.expire_date = item['_source']['expire_date']


            # data class set dict
            prod_list.set_date_dict()
            return prod_list

# 전체 상품 벌크실행
# DataMallProdList().insertbulk_whole()
#신상품 벌크실행
# DataMallProdList().insertbulk_newprod()

# 모든 wholepage 서치 하기
# DataMallProdList().getAllProdlist()
# a= DataMallProdList()
# a.search_prod_num()
#
# a.result_all_data(a.search_prod_num())
# DataMallProdList().__init__()