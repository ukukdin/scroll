from elasticsearch_dsl import Document, Integer, Keyword, connections,Text,Date
import Crawling.common.util_common as cu
from Crawling.common.lib_es import LibES


esip ='192.168.0.41:9200'
connections.create_connection(hosts=[esip])

class DataNewProdIndex(Document):
    # 코드명 이름
    code_mall = Keyword()
    # 몰 이름
    name_mall = Keyword()
    # 몰 코드명
    name_code_mall = Keyword()
    # 카테고리
    # mall_category = Keyword()
    # 상품번호
    new_prod_num = Keyword()
    # 상품이름
    new_prod_name = Text()
    # 상품가격
    new_prod_price = Integer()
    # 상품 입력 날짜
    new_prod_date = Date()


    class Index:
        code = cu.getDateMonth()
        name = 'newprod'
        setting={
            'number_of_shards':1,

        }

    def save(self, **kwargs):
        return super(DataNewProdIndex, self).save(**kwargs)


if __name__ == '__main__':
    re_index_name = 'newprod'

    # delete index
    libes = LibES()
    libes.deleteIndex(re_index_name)
    print(re_index_name + ': delete index!')

    # create Index
    DataNewProdIndex()
    DataNewProdIndex.init()
    print(re_index_name + " : create index! done")