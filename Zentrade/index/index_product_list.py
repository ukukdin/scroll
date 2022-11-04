from elasticsearch_dsl import Document, Integer, Keyword, connections,Text,Date,Nested
import Crawling.common.util_common as cu
from Crawling.common.lib_es import LibES


esip ='192.168.0.43:9200'
# esip = '127.0.0.1:9200'
connections.create_connection(hosts=[esip])
class DataWholepageIndex(Document):
    product_listed=Nested(include_in_parent=True,
            properties={
                # 코드명 이름
                'code_mall': Keyword(),
                # 몰 이름
                'name_mall': Keyword(),
                # 몰 코드명
                'name_code_mall': Keyword(),
                # 상품리스트 url
                'prodlist_url': Keyword(),
                # 상품명
                'prod_num': Keyword(),
                # 상품이름
                'prod_name': Text(),
                # 상품가격
                'prod_price': Integer(),
    'product_detail' : Nested(properties={
        # 코드명 이름
        'code_mall': Keyword(),
        # 몰 이름
        'name_mall': Keyword(),
        # 몰 코드명
        'name_code_mall': Keyword(),
        # 상품리스트 url
        'prod_detail_url': Keyword(),
        'category': Keyword(),
        # 상품명
        'prod_num': Keyword(),
        # 상품이름
        'prod_name': Text(),
        # 상품가격
        # 상품가격
        'prod_price': Integer(),
        'prod_date': Text(),
        # 원산지
        'country': Keyword(),
        # 과세여부
        'prod_tax': Text(),
        # 배송비
        'deli_price': Integer(),
        # 배송 디테일
        'deli_detail1': Text(),
        'deli_detail2': Text(),
        # 선택 옵션
        # 'option' : self.option,
        # 변동내용: 변경항목,상세내용,변경일시
        'changedlist': Text(),
        'detail_tax': Text(),
        'change_dete': Text()
    })})





    class Index():
        code = cu.getDateMonth()
        name = 'product_list'
        setting = {
            'number_of_shards': 1,
         }


    def save(self, **kwargs):
        return super(DataWholepageIndex, self).save(**kwargs)


if __name__ == '__main__':
    # 상품 리스트
    re_index_name = 'product_list'


    # 상품 리스트1
    if re_index_name =='product_list':
        # delete index
        libes = LibES()
        libes.deleteIndex(re_index_name)
        print(re_index_name + ': delete index!')

        # create Index
        DataWholepageIndex()
        DataWholepageIndex.init()
        print(re_index_name + " : create index! done")
