from elasticsearch import Elasticsearch
from elasticsearch_dsl import Document
from elasticsearch import helpers
import Crawling.common.util_common as cu
from Zentrade.zen import Out_product, New_product,Product_detail,Product_list
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
        # 신상품 페이지
        # self.n = New_product.New_List()
        # #신상품 페이지 값
        # self.np =self.n.NP()
        # # 품절 페이지
        # self.o = Out_product.out_of_stock()
        # # 품절 페이지값
        # self.op =self.o.outstock()
        # 상세상품 페이지
        self.p = Product_detail.Product_List()
        self.pl = self.p.prod_list()
        # 상세상품 페이지값

        self.es = Elasticsearch('[127.0.0.1]:9200')


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
        index = 'newproductlist'
        for a in self.no:
            self.Wname = a[:][1].string
            print(self.Wname)
            self.Wnum = a[:][0]
            self.Wprice=a[:][2].replace(",","")
            docs.append({
               '_index':'newproductlist',
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
    # def insertProductlistW(self,dataone):
    #     newDocs=[]
    #     for No in dataone:
    #         docone = No.get_data_dict1()
    #
    #         doc = {'_index':self.indexname,'_source': docone}
    #         newDocs.append(doc)
    #     helpers.bulk(self.es,newDocs,index=self.indexname)

    # 신상품 bulk 로 실행
    #
    # def insertbulk_newprod(self):
    #     newDoc=[]
    #     index = 'newprod'
    #
    #     for b in self.np:
    #         new_name = b[1]
    #         new_num = b[0]
    #         new_date = b[3]
    #         new_price = b[2].replace(",", "")
    #         newDoc.append({
    #             '_index':'newprod',
    #             '_source':{
    #             'name_mall': self.n.name_mall,
    #              'name_code_mall': self.n.name_code_mall,
    #             'code_mall': self.n.code_mall,
    #             'new_prod_num':new_num,
    #             'new_prod_name':new_name,
    #             'new_prod_price':new_price,
    #             'new_prod_date':new_date,
    #             '@timestamp':cu.getDateToday()
    #             }
    #         })
    #     helpers.bulk(self.es,newDoc,index=index)
    #
    #
    def insertbulk_prod_detail(self):
        newProdDoc=[]
        index = 'productdetail'

        for prod in self.pl:
            prod_num = prod[:][0]
            prod_name = prod[:][1]
            category = prod[:][2]
            prod_price = prod[:][3]
            country = prod[:][4]
            prod_tax =prod[:][5]
            deli_price = prod[:][6]
            deli_detail1 = prod[:][7]
            deli_detail2 =prod[:][8]
            # option = prod[:][9]
            changedlist = prod[:][9]
            detail_tax = prod[:][10]
            change_dete =prod[:][11]
            newProdDoc.append({
                    '_index':'productdetail',
                    '_source':{
                    'name_mall': self.p.name_mall,
                     'name_code_mall': self.p.name_code_mall,
                    'code_mall': self.p.code_mall,
                    # 카테고리
                    'category': category,
                    # 상품명
                    'prod_num': prod_num,
                    # 상품이름
                    'prod_name': prod_name,
                    # 상품가격
                    'prod_price': prod_price,
                    # 원산지
                    'country': country,
                    # 과세여부
                    'prod_tax': prod_tax,
                    # 배송비
                    'deli_price': deli_price,
                    # 배송 디테일
                    'deli_detail1': deli_detail1,
                    'deli_detail2': deli_detail2,
                    # 'option': option,

                    # 변동내용: 변경항목,상세내용,변경일시
                    'changedlist': changedlist,
                    'detail_tax': detail_tax,
                    'change_dete': change_dete,
                    '@timestamp':cu.getDateToday()
                }
            })
        helpers.bulk(self.es, newProdDoc, index=index)
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
    #         prod_list.reorder = item['_source']['reorder']
    #         prod_list.reorder_date = item['_source']['reorder_date']
    #
    #         prod_list.expire_date = item['_source']['expire_date']
    #
    #
    #         # data class set dict
    #         prod_list.set_date_dict()
    #         return prod_list

DataMallProdList().__init__()
# DataMallProdList().insertbulk_whole()
DataMallProdList().insertbulk_prod_detail()