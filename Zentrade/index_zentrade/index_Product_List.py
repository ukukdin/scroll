from elasticsearch_dsl import Document, Integer, Keyword, connections,Text,Date
import Crawling.common.util_common as cu
from Crawling.common.lib_es import LibES


esip ='192.168.0.41:9200'
connections.create_connection(hosts=[esip])

class DataProductListIndex(Document):
    # 코드명 이름
    code_mall = Keyword()
    # 몰 이름
    name_mall = Keyword()
    # 몰 코드명
    name_code_mall = Keyword()
    # 카테고리
    category = Keyword()
    # 상품명
    prod_num = Keyword()
    # 상품이름
    prod_name = Text()
    # 카테고리
    category = Keyword()
    # 상품가격
    prod_price = Integer()
    # 원산지
    country = Keyword()
    # 과세여부
    prod_tax = Text()

    # 배송비
    deli_price = Integer()
    # 배송 디테일
    deli_detail1 = Text()
    deli_detail2 =Text()
    option = Text()
    # 변동내용: 변경항목,상세내용,변경일시
    changedlist = Text()
    detail_tax = Text()
    change_dete =Text()

    class Index:
        code = cu.getDateMonth()
        name = 'prodlist'
        setting={
            'number_of_shards':1,

        }

    def save(self, **kwargs):
        return super(DataProductListIndex, self).save(**kwargs)


if __name__ == '__main__':
    re_index_name = 'prodlist'

    # delete index
    libes = LibES()
    libes.deleteIndex(re_index_name)
    print(re_index_name + ': delete index!')

    # create Index
    DataProductListIndex()
    DataProductListIndex.init()
    print(re_index_name + " : create index! done")