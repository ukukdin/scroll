from elasticsearch import Elasticsearch
from elasticsearch_dsl import Document
from elasticsearch import helpers
import Crawling.common.util_common as cu
from Zentrade.zen import Out_product,Product_list
from Zentrade.libara.zen_data import DataZenProduct
from Zentrade.libara.zen_prodlist_data import DataZenProductList

class DataMallProdList(Document):
    def __init__(self):
        super(DataMallProdList, self).__init__()
        # 전체페이지
        #
        self.w = Product_list.Whole_list()

        # 전체페이지에서 값
        self.no = self.w.parser_wholelist()
        # print(self.no)

        # # # 품절 페이지
        # # self.o = Out_product.out_of_stock()
        # # # 품절 페이지값
        # # self.op =self.o.outstock()
        # # 상세상품 페이지
        # self.p = Product_detail.Product_List()
        # self.pl = self.p.prod_list()
        # # 상세상품 페이지값

        self.es = Elasticsearch('[192.168.0.41]:9200')


    # 하나만 실행
    # def insertone(self):
    #     index = 'wholepage'
    #     doc={
    #         "prod_num":"num",
    #         "prod_name":"",
    #         "prod_price":120333,
    #         "@timestamp":cu.getDateToday()
    #     }
    #     self.es.index(index=index,doc_type="_doc",body=doc)
    # 벌크 넣고 실행
    def insertbulk_whole(self):
        docs = []
        index = 'productlist'
        for a in self.no:
            name = a[:][1].string
            print(self.Wname)
            num = a[:][0]
            price=a[:][2].replace(",","")
            docs.append({
               '_index':'productlist',
                '_source':{
                   'name_mall': self.w.name_mall,
                   'name_code_mall': self.w.name_code_mall,
                   'code_mall':self.w.code_mall,
                   'prod_num':num,
                   'prod_name':name,
                   'prod_price':price,
                   '@timestamp':cu.getDateToday()
                    }
            })
        helpers.bulk(self.es,docs,index=index)

    # def insertProductlistW(self,dataone):
    #     newDocs=[]
    #     for No in dataone:
    #         docone = No.get_data_dict1()
    #
    #         doc = {'_index':self.indexname,'_source': docone}
    #         newDocs.append(doc)
    #     helpers.bulk(self.es,newDocs,index=self.indexname)



    #
    # # 전체 가져오기
    # def getAllProdlist(self):
    #     index = 'wholepage'
    #     try:
    #         body ={"query":
    #                    {'match_all':{self.Wnum}}
    #
    #                }
    #         res=self.es.search(index=index,body=body,size=10000)
    #         return res
    #     except Exception as ex:
    #         print("zentrade_whole_list: ",ex)
    # # 넙버 값으로 원하는 값 찾기
    # def search_prod_name(self,name):
    #     index = 'wholepage'
    #     body ={
    #             "query":{
    #               "bool":{
    #                 "must":[
    #                   {"match":{"prod_name":name}}
    #                     ]
    #             }
    #         }
    #     }
    #
    #     res = self.es.search(index=index,body=body,size=10000)
    #     return res
    # 전체 상품 리스트
    # def result_all_productList(self, res):
    #     all_data_model = []
    #     for item in res['hits']['hits']:
    #         # class
    #         prod_list = DataZenProductList()
    #         prod_list.timestamp = item['_source']['@timestamp']
    #         prod_list.code_mall = item['_source']['code_mall']
    #         prod_list.name_mall = item['_source']['name_mall']
    #         prod_list.name_code_mall = item['_source']['name_code_mall']
    #         prod_list.prod_num = item['_source']['prod_num']
    #         prod_list.prod_name = item['_source']['prod_name']
    #
    #         prod_list.prod_price = item['_source']['prod_price']
    #         prod_list.country = item['_source']['country']
    #         prod_list.prod_tax = item['_source']['prod_tax']
    #         prod_list.deli_price = item['_source']['deli_price']
    #         prod_list.deli_detail1 = item['_source']['deli_detail1']
    #         prod_list.deli_detail2 = item['_source']['deli_detail2']
    #
    #         prod_list.changedlist = item['_source']['changedlist']
    #         prod_list.detail_tax = item['_source']['detail_tax']
    #         prod_list.change_dete = item['_source']['change_dete']
    #         prod_list.new_prod_date = item['_source']['new_prod_date']
    #         # data class set dict
    #         prod_list.set_date_dict()
    #         all_data_model.append(prod_list)
    #
    #     return all_data_model
    #
    # def result_all_data_product(self, res):
    #     all_data_model = []
    #     for item in res['hits']['hits']:
    #         # class
    #         prod_list = DataZenProduct()
    #         prod_list.timestamp = item['_source']['@timestamp']
    #         prod_list.code_mall = item['_source']['code_mall']
    #         prod_list.name_mall = item['_source']['name_mall']
    #         prod_list.name_code_mall = item['_source']['name_code_mall']
    #         prod_list.prod_num = item['_source']['prod_num']
    #         prod_list.prod_name = item['_source']['prod_name']
    #
    #         prod_list.prod_price = item['_source']['prod_price']
    #         # prod_list.prod_out = item['_source']['prod_out']
    #         # prod_list.reason = item['_source']['reason']
    #         # prod_list.reorder = item['_source']['reorder']
    #         # prod_list.reorder_date = item['_source']['reorder_date']
    #         #
    #         # prod_list.expire_date = item['_source']['expire_date']
    #
    #         # data class set dict
    #         prod_list.set_date_dict()
    #         all_data_model.append(prod_list)
    #
    #     return all_data_model
    # # def result_all_name(self, item):
    #
    # def result_one_data1(self, item):
    #         # class
    #         prod_list = DataZenProduct()
    #         prod_list.timestamp = item['_source']['@timestamp']
    #         prod_list.code_mall = item['_source']['code_mall']
    #         prod_list.name_mall = item['_source']['name_mall']
    #         prod_list.name_code_mall = item['_source']['name_code_mall']
    #         prod_list.mall_category = item['_source']['mall_category']
    #         prod_list.prod_num = item['_source']['prod_num']
    #         prod_list.prod_name = item['_source']['prod_name']
    #
    #         prod_list.prod_price = item['_source']['prod_price']
    #         prod_list.prod_out = item['_source']['prod_out']
    #         prod_list.reason = item['_source']['reason']
    #         prod_list.reorder = item['_source']['reorder']s
    #         prod_list.reorder_date = item['_source']['reorder_date']
    #
    #         prod_list.expire_date = item['_source']['expire_date']
    #
    #
    #         # data class set dict
    #         prod_list.set_date_dict()
    #         return prod_list

DataMallProdList().__init__()
DataMallProdList().insertbulk_whole()
# DataMallProdList().insertbulk_prod_detail()