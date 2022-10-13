from elasticsearch_dsl import Document, Integer, Keyword, connections,Text,Date
import Crawling.common.util_common as cu
from Crawling.common.lib_es import LibES


esip ='192.168.0.41:9200'
connections.create_connection(hosts=[esip])

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
    # Whole_prod_url = Keyword()
    # 재고여부
    prod_out = Keyword()
    # 품절 이유
    reason = Text()
    # 재입고 여부
    reorder = Text()
    # 재입고 예정일
    reorder_date = Text()
    # 삭제예정일
    expire_date = Text()


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

    # delete index
    libes = LibES()
    libes.deleteIndex(re_index_name)
    print(re_index_name + ': delete index!')

    # create Index
    DataWholepageIndex()
    DataWholepageIndex.init()
    print(re_index_name + " : create index! done")