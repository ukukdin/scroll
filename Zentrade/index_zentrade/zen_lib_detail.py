from elasticsearch import Elasticsearch
from elasticsearch_dsl import Document
from elasticsearch import helpers
import Crawling.common.util_common as cu
from Zentrade.zen import Out_product, New_product,Product_detail,Product_list

class DataMallProddetail(Document):
    def __init__(self):
        super(DataMallProddetail, self).__init__()
    #  상세상품 페이지
        self.p = Product_detail.Product_List()
        self.pl = self.p.prod_list()

        self.es = Elasticsearch('[192.168.0.41]:9200')

        # 상세 상품 리스트
        def insertbulk_prod_detail(self):
            newProdDoc = []
            index = 'productdetail'

            for prod in self.pl:
                prod_num = prod[:][0]
                prod_name = prod[:][1]
                category = prod[:][2]
                prod_price = prod[:][3]
                country = prod[:][4]
                prod_tax = prod[:][5]
                deli_price = prod[:][6]
                deli_detail1 = prod[:][7]
                deli_detail2 = prod[:][8]
                # option = prod[:][9]
                changedlist = prod[:][9]
                detail_tax = prod[:][10]
                change_dete = prod[:][11]
                print(prod_name)
                newProdDoc.append({
                    '_index': 'productdetail',
                    '_source': {
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
                        '@timestamp': cu.getDateToday()
                    }
                })
            helpers.bulk(self.es, newProdDoc, index=index)

            # # 넙버 값으로 원하는 값 찾기
            # def search_prod_name(self,name):
            #     index = 'productdetail'
            #     body ={
            #             "query":{
            #               "bool":{
            #                 "must":[
            #                   {"match":{"prod_name":name}}
            #                     ]
            #             }
            #         }
            #     }
            # res = self.es.search(index=index, body=body, size=10000)
            #     return res