
# import onch_info as Info
import Crawling.common.util_common as cu
from elasticsearch_dsl import Document, Integer, Keyword, connections
from Crawling.common.lib_es import LibES

esip = '192.168.0.41:9200'
# esip = '127.0.0.1:9200'
connections.create_connection(hosts=[esip])

class DataMallProdlistIndex(Document):
    # Prod List : 6
    # 1 몰 code
    code_mall = Keyword()
    # 2 몰 name
    name_mall = Keyword()
    # 3 몰 name codeWS
    name_code_mall = Keyword()
    # 4 상품리스트 분류 코드
    prodlist_category = Keyword()
    # 5 상품리스트 분류명
    prodlist_category_name = Keyword()
    # 6 상품리스트 URL
    prodlist_url = Keyword()

    # Production : 9
    # 7 hit 상품 code
    code_prod_hit = Keyword()
    # 8 몰 상품 code
    code_prod_origin = Keyword()
    # 9 상품명
    prod_name = Keyword()
    # 10 상품가격
    prod_price = Integer()
    # 11 상품상태 : 판매중/일시품절/품절
    prod_sta = Keyword()

    # 12 입점일
    in_date = Keyword()
    # 13 main image
    main_image = Keyword()
    # 14 detail url
    detail_url = Keyword()
    # 15 상품개수
    prod_unit = Keyword()

    ########################
    class Index:
        # code = '2021-11'
        code = cu.getDateMonth()
        name = 'mall_prodlist'
        settings={
            "number_of_shards": 1,
        }

    def save(self, ** kwargs):
        return super(DataMallProdlistIndex, self).save(** kwargs)

if __name__ == '__main__':
    # code = '2021-11'
    code = cu.getDateMonth()
    #####################

    # if code == 'test':
    # index name
    mall_rename_prod_index = 'mall_prodlist'

    # delete index
    libes = LibES()
    libes.deleteIndex(mall_rename_prod_index)
    print(mall_rename_prod_index + ': delete index!')

    # create index
    DataMallProdlistIndex()
    DataMallProdlistIndex.init()
    print(mall_rename_prod_index + ': create index!')

