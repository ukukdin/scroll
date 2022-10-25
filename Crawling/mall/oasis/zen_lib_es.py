from elasticsearch import Elasticsearch
from elasticsearch_dsl import Document
from elasticsearch import helpers
from Zentrade.zen_new_product.data_new_product_list import DataZenProduct


class DataMallProdList(Document):
    def __init__(self):
        super(DataMallProdList, self).__init__()
        self.es = Elasticsearch('[192.168.0.41]:9200')
        self.index = 'productlist'

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
    def insertbulk_whole(self,onedoc):
        docs = []

        for i in onedoc:
            print(i)
            doc = {'_index':self.index,'_source':i}
            docs.append(doc)

        helpers.bulk(self.es,docs,index=self.index)

    # 전체 가져오기
    def getAllProdlist(self,prodnum,indexname):
        try:
            body ={"query":
                       {'match_all':{prodnum}}
                   }
            res=self.es.search(index=indexname,body=body,size=10000)
            return res
        except Exception as ex:
            print("zentrade_whole_list: ",ex)

    # 넙버 값으로 원하는 값 찾기
    def search_prod_name(self,name):
        index = 'wholepage'
        body ={
                "query":{
                  "bool":{
                    "must":[
                      {"match":{"prod_name":name}}
                        ]
                }
            }
        }
        res = self.es.search(index=index,body=body,size=10000)
        return res

    # 전체 상품 리스트


    def result_all_data_product(self, res):
        all_data_model = []
        for item in res['hits']['hits']:
            # class
            prod_list = DataZenProduct()
            prod_list.timestamp = item['_source']['@timestamp']
            prod_list.code_mall = item['_source']['code_mall']
            prod_list.name_mall = item['_source']['name_mall']
            prod_list.name_code_mall = item['_source']['name_code_mall']
            prod_list.prod_num = item['_source']['prod_num']
            prod_list.prod_name = item['_source']['prod_name']
            prod_list.prod_price = item['_source']['prod_price']
            prod_list.prod_date = item['_source']['prod_date']
            prod_list.prod_out = item['_source']['prod_out']
            prod_list.reason = item['_source']['reason']
            prod_list.reorder = item['_source']['reorder']
            prod_list.reorder_date = item['_source']['reorder_date']
            prod_list.expire_date = item['_source']['expire_date']

            # data class set dict
            prod_list.set_date_dict()
            all_data_model.append(prod_list)

        return all_data_model

    def result_one_data1(self, item):
        # class
        prod_list = DataZenProduct()
        prod_list.timestamp = item['_source']['@timestamp']
        prod_list.code_mall = item['_source']['code_mall']
        prod_list.name_mall = item['_source']['name_mall']
        prod_list.name_code_mall = item['_source']['name_code_mall']
        prod_list.category = item['_source']['category']
        prod_list.prod_num = item['_source']['prod_num']
        prod_list.prod_name = item['_source']['prod_name']
        prod_list.prod_price = item['_source']['prod_price']
        prod_list.prod_date = item['_source']['prod_date']
        prod_list.prod_out = item['_source']['prod_out']
        prod_list.reason = item['_source']['reason']
        prod_list.reorder = item['_source']['reorder']
        prod_list.reorder_date = item['_source']['reorder_date']
        prod_list.expire_date = item['_source']['expire_date']

        # data class set dict
        prod_list.set_date_dict()
        return prod_list

