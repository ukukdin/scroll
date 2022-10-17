from elasticsearch import Elasticsearch
from elasticsearch_dsl import Document
from elasticsearch import helpers
import Crawling.common.util_common as cu


class DataMallProddetail(Document):
    def __init__(self):
        super(DataMallProddetail, self).__init__()
    #  상세상품 페이지
        # self.es = Elasticsearch('192.168.0.1:9200')
        self.es = Elasticsearch('127.0.0.1:9200')
        self.index ='productdetail'

        # 상세 상품 리스트
    def insertbulk_prod_detail(self,detail):
        newProdDoc = []
        for i in detail:
            doc={'_index':self.index,'_source':i}
            newProdDoc.append(doc)
        helpers.bulk(self.es,newProdDoc,index=self.index)
        print("완료!!")
