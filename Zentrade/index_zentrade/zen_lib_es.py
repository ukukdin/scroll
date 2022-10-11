from elasticsearch import Elasticsearch
from elasticsearch import helpers
import Crawling.common.util_common as cu
from Zentrade import WholePage as wp
import json

class DataMallProdList():
    def __init__(self):
        super(DataMallProdList, self).__init__()

        self.x = wp.Whole_list()
        self.no = self.x.parser_wholelist()
        self.es = Elasticsearch('[192.168.0.41]:9200')

    # 벌크 넣고 실행
    def insertbulk(self):
        with open('mapping.json', 'r') as f:
            mapping = json.load(f)
        docs=[]
        for a in self.no:
            name = a[:][1].string
            num = a[:][0]
            price=a[:][2]
            docs.append({
               '_index':'wholepage',
                '_source':{
               'prod_num':num,
               'prod_name':name,
               'prod_price':price,
               '@timestamp':cu.getDateToday()
                }
            })
        helpers.bulk(self.es,docs)

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


# 벌크실행
DataMallProdList().insertbulk()


# 모든 wholepage 서치 하기
# DataMallProdList().getAllProdlist()