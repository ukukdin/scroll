from elasticsearch import Elasticsearch
from elasticsearch_dsl import Document, Integer, Keyword, connections,Text,Date
from elasticsearch import helpers
import Crawling.common.util_common as cu
from Zentrade import New_prod,OutofStock
from Zentrade import WholePage
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
            name = a[:][1].string
            num = a[:][0]
            price=a[:][2].replace(",","")
            docs.append({
               '_index':'wholepage',
                '_source':{
               'prod_num':num,
               'prod_name':name,
               'prod_price':price,
               '@timestamp':cu.getDateToday()
                }
            })
        helpers.bulk(self.es,docs,index=index)
    def insertbulk_newprod(self):
        newDoc=[]
        index = 'newprod'
        for b in self.np:
            new_name = b[0]
            new_num = b[1]
            new_date = b[2]
            new_price =b[3].replace(",","")
            newDoc.append({
                '_index':'newprod',
                '_source':{
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
                       {'match_all':{}}

                   }
            res=self.es.search(index=index,body=body,size=10000)
            return res
        except Exception as ex:
            print("zentrade_whole_list: ",ex)
    # 넙버 값으로 원하는 값 찾기
    def search_prod_num(self,num):
        index = 'wholepage'
        body ={
                "query":{
                    "bool":{
                        "must":[
                            {"match":{"num_of_prod":num}}
                        ]
                    }
                }
        }
        res = self.es.search(index=index,body=body,size=10000)
        return res


# 전체 상품 벌크실행
# DataMallProdList().insertbulk_whole()
#신상품 벌크실행
DataMallProdList().insertbulk_newprod()

# 모든 wholepage 서치 하기
# DataMallProdList().getAllProdlist()