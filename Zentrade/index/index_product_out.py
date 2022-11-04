from elasticsearch_dsl import Document, Integer, Keyword, connections,Text,Date
import Crawling.common.util_common as cu
from Crawling.common.lib_es import LibES


esip ='192.168.0.43:9200'
# esip = '127.0.0.1:9200'
connections.create_connection(hosts=[esip])

class DataMallProddetail(Document):
    # 코드명 이름
    code_mall = Keyword()
    # 몰 이름
    name_mall = Keyword()
    # 몰 코드명
    name_code_mall = Keyword()
    # 상품리스트 url
    prod_out_url = Keyword()
    # 카테고리
    category = Keyword()
    # 상품명
    prod_num = Keyword()
    # 상품이름
    prod_name = Text()
    # 상품가격
    prod_price = Integer()
    # 상품 입력 날짜
    prod_date = Text()
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
        name = 'out_product'

        setting = {
            'number_of_shards': 1,
        }

    def save(self, **kwargs):
        return super(DataWholepageIndex, self).save(**kwargs)


if __name__ == '__main__':

    # # 품절 리스트
    re_index_name = 'out_product'
   


    # 품절 리스트
    if re_index_name == 'out_product' :
        # delete index
        libes = LibES()
        libes.deleteIndex(re_index_name)
        print(re_index_name + ': delete index!')

        # create Index
        DataWholepageIndex()
        DataWholepageIndex.init()
        print(re_index_name + " : create index! done")