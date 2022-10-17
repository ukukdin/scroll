
from elasticsearch import Elasticsearch
from elasticsearch import helpers

from Zentrade.libara.zen_prodlist_detail import DataZenProductList

class DataMallNewProduct():
    def __init__(self):
        super(DataMallNewProduct, self).__init__()
        self.esip = '127.0.0.1:9200'

        self.es = Elasticsearch(self.esip)
        self.index = 'newproductlist'
    # 신상품 bulk 로 실행
    def insertbulk_newprod(self,np):
        newDoc = []
        doc = {'_index':self.index,'_source':np}
        newDoc.append(doc)

        helpers.bulk(self.es,newDoc,index=self.index)

    # def result_all_data_product(self, res):
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
    #         prod_list.prod_price = item['_source']['prod_price']
    #         prod_list.prod_out = item['_source']['prod_out']
    #         prod_list.reason = item['_source']['reason']
    #         prod_list.reorder = item['_source']['reorder']
    #         prod_list.reorder_date = item['_source']['reorder_date']
    #
    #         prod_list.expire_date = item['_source']['expire_date']
    #
    #         # data class set dict
    #         prod_list.set_date_dict()
    #         all_data_model.append(prod_list)
    #
    #     return all_data_model
    # def result_all_name(self, item):
# DataMallNewProduct().__init__()