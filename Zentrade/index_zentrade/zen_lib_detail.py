from elasticsearch import Elasticsearch
from elasticsearch_dsl import Document
from elasticsearch import helpers
from Zentrade.zen_new_product.data_new_Product_detail import DataZenProductList
from Zentrade.zen_new_product.data_new_product_list import DataProductNewList
from Zentrade.zen_product.data_prodlist_detail import DataProdlist_detail
from Zentrade.zen_product_out.data_product_out import DataProductOut
from Zentrade.zen_product.data_product_list import DataProductList


class DataMallProddetail(Document):
    def __init__(self):
        super(DataMallProddetail, self).__init__()
    #  상세상품 페이지
        self.es = Elasticsearch('192.168.0.41:9200')

        # self.es = Elasticsearch('127.0.0.1:9200')

        # 상세 상품 리스트
    def insertbulk_prod(self,detail,indexname):
        newProdDoc = []
        for i in detail:
            doc={'_index':indexname,'_source':i}
            newProdDoc.append(doc)
        helpers.bulk(self.es,newProdDoc,index=indexname)
        print("완료!!")
        # search : mall_code

    # code_mall
    def search_mall_code(self, prod_num,index_name):
        body = {
            "query": {
                "bool": {
                    "must": [
                        {"match": {"prod_num": prod_num}}

                    ]
                }
            }

        }


        res = self.es.search(index=index_name, body=body, size=10000)

        return res
    # update
    def update_mall_code(self,prod_out,indexname,ids):
        body= {
            "doc":{"prod_out": prod_out}
        }
        res =  self.es.update(index=indexname,body=body,id=ids)
        return res
        # update

    def update_mall_coded(self, new_prod, indexname, ids):
        newProdDoc = []
        for i in new_prod:
            doc = {'_source': i}
            newProdDoc.append(doc)
        
        res = self.es.update(index=indexname, body=doc, id=ids)
        print('완료')
        return res
    # 전체 상품 검색
    def getAllProddetail(self,indexname):
        try:
            body = {"query": {"match_all": {}},
                    "sort": {
                        "@timestamp": {"order": "DESC"}
                    }}
            res = self.es.search(index=indexname, body=body, size=10000)
            return res
        except Exception as ex:
            print('es_oasis_prod - getAllProdlist :', ex)

    # 상품 상세 리스트
    def result_all_productdetail(self, res):
        all_data_model = []
        for item in res['hits']['hits']:
            # class
            prod_list = DataZenProductList()
            prod_list.timestamp = item['_source']['@timestamp']
            prod_list.code_mall = item['_source']['code_mall']
            prod_list.name_mall = item['_source']['name_mall']
            prod_list.name_code_mall = item['_source']['name_code_mall']
            prod_list.prod_category = item['_source']['category']
            prod_list.prod_num = item['_source']['prod_num']
            prod_list.prod_name = item['_source']['prod_name']
            prod_list.prod_price = item['_source']['prod_price']
            prod_list.prod_date = item['_source']['prod_date']
            prod_list.country = item['_source']['country']
            prod_list.prod_tax = item['_source']['prod_tax']
            prod_list.deli_price = item['_source']['deli_price']
            prod_list.deli_detail1 = item['_source']['deli_detail1']
            prod_list.deli_detail2 = item['_source']['deli_detail2']
            prod_list.changedlist = item['_source']['changedlist']
            prod_list.detail_tax = item['_source']['detail_tax']
            prod_list.change_dete = item['_source']['change_dete']
            # data class set dict
            prod_list.set_date_dict()
            all_data_model.append(prod_list)

        return all_data_model
    # 상품 상세 리스트 개별
    def result_one_data(self, item):
        # class
        prod_list = DataZenProductList()
        prod_list.timestamp = item['_source']['@timestamp']
        prod_list.code_mall = item['_source']['code_mall']
        prod_list.name_mall = item['_source']['name_mall']
        prod_list.name_code_mall = item['_source']['name_code_mall']
        prod_list.prod_category = item['_source']['category']
        prod_list.prod_num = item['_source']['prod_num']
        prod_list.prod_name = item['_source']['prod_name']
        prod_list.prod_price = item['_source']['prod_price']
        # prod_list.new_prod_date = item['_source']['prod_date']
        prod_list.country = item['_source']['country']
        prod_list.prod_tax = item['_source']['prod_tax']
        prod_list.deli_price = item['_source']['deli_price']
        prod_list.deli_detail1 = item['_source']['deli_detail1']
        prod_list.deli_detail2 = item['_source']['deli_detail2']
        prod_list.changedlist = item['_source']['changedlist']
        prod_list.detail_tax = item['_source']['detail_tax']
        prod_list.change_dete = item['_source']['change_dete']

        # data class set dict
        prod_list.set_date_dict()
        return prod_list

    # 상품 리스트 한번에
    def result_all_data_product(self, res):
        all_data_model = []
        for item in res['hits']['hits']:
            # class
            prod_list = DataProductList()
            prod_list.timestamp = item['_source']['@timestamp']
            prod_list.code_mall = item['_source']['code_mall']
            prod_list.name_mall = item['_source']['name_mall']
            prod_list.name_code_mall = item['_source']['name_code_mall']
            prod_list.prodlist_url= item['_source']['prodlist_url']
            prod_list.prod_num = item['_source']['prod_num']
            prod_list.prod_name = item['_source']['prod_name']
            prod_list.prod_price = item['_source']['prod_price']

            # data class set dict
            prod_list.set_date_dict()
            all_data_model.append(prod_list)
        return all_data_model
    # 전체 상품 리스트 값 하나 넣기
    def result_one_data_product(self, item):
        # class

        prod_list = DataProductList()
        prod_list.timestamp = item['_source']['@timestamp']
        prod_list.code_mall = item['_source']['code_mall']
        prod_list.name_mall = item['_source']['name_mall']
        prod_list.name_code_mall = item['_source']['name_code_mall']
        prod_list.prodlist_url = item['_source']['prodlist_url']
        prod_list.prod_num = item['_source']['prod_num']
        prod_list.prod_name = item['_source']['prod_name']
        prod_list.prod_price = item['_source']['prod_price']

        # data class set dict
        prod_list.set_date_dict()
        return prod_list
    # 품절 상품 검색 한번에
    def result_all_data_outproduct(self, res):
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
            # prod_list.prod_out = item['_source']['prod_out']
            prod_list.reason = item['_source']['reason']
            prod_list.reorder = item['_source']['reorder']
            prod_list.reorder_date = item['_source']['reorder_date']
            prod_list.expire_date = item['_source']['expire_date']

            # data class set dict
            prod_list.set_date_dict()
            all_data_model.append(prod_list)
        return all_data_model
    # 품절 리스트 개별
    def result_one_data_outproduct(self, item):
        # class
        prod_list = DataProductOut()
        prod_list.timestamp = item['_source']['@timestamp']
        prod_list.code_mall = item['_source']['code_mall']
        prod_list.name_mall = item['_source']['name_mall']
        prod_list.name_code_mall = item['_source']['name_code_mall']
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
        # 상품 리스트 개별


    # 새로운 상품리스트
    def result_all_data_newproduct(self, res):
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

            # data class set dict
            prod_list.set_date_dict()
            all_data_model.append(prod_list)
        return all_data_model

    # 새로운 리스트 개별
    def result_one_data1(self, item):
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

        # data class set dict
        prod_list.set_date_dict()
        return prod_list