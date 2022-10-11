from elasticsearch_dsl import Document, Integer, Keyword, connections,Text
import Crawling.common.util_common as cu
from elasticsearch import Elasticsearch,helpers
import datetime
import json

esip ='192.168.0.41:9200'

connections.create_connection(host=[esip])

class DataWholepageIndex(Document):
    # 코드명 이름
    code_mall = Keyword()
    # 몰 이름
    name_mall = Keyword()
    # 몰 코드명
    name_code_mall = Keyword()
    # 카테고리
    mall_category = Keyword()
    # 상품명
    prod_num = Keyword()
    # 상품이름
    prod_name = Text()
    # 상품가격
    prod_price = Integer()
    # 상품전체 URL
    Whole_prod_url = Keyword()

    class Index:
        code = cu.getDateMonth()
        name = 'wholepage'
        setting={
            'number_of_shards':1,

        }

    def save(self, **kwargs):
        return super(DataWholepageIndex, self).save(**kwargs)


if __name__ == '__main__':
    re_index_name = 'wholepage'

    # create Index
    DataWholepageIndex()
    DataWholepageIndex.init()
    print(re_index_name + " : create index! done")