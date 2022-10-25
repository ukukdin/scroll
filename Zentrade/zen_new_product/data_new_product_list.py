# 상품 리스트 + 신상품 리스트 + 품절 리스트
class DataProductNewList:
    def __init__(self):
        self.data_dict = {}
        self.data_list = []

        self.timestamp = None

        # 몰 code
        self.code_mall = None

        # 몰 name
        self.name_mall = None

        # 몰 name code
        self.name_code_mall = None
        # 신상품 리스트 url
        self.new_prodlist_url = None

        # 상품 번호
        self.prod_num = None
        # 상품명
        self.prod_name = None

        # 상품가격
        self.prod_price = None
        # 신상품 입고 날짜
        self.prod_date = None


    def get_date_dict(self):
        return self.data_dict

    def set_date_dict(self):
        self.data_dict = {
            '@timestamp': self.timestamp,
            # 6
            # 몰 code
            'code_mall': self.code_mall,
            # 몰 name
            'name_mall': self.name_mall,
            # 몰 name code
            'name_code_mall': self.name_code_mall,
            # 신상품 리스트 url
            'new_prodlist_url':self.new_prodlist_url,
            # 상품명
            'prod_num':self.prod_num,
            # 상품이름
            'prod_name':self.prod_name,
            # 상품가격
            'prod_price': self.prod_price,
            # 신상품 입고날짜
            'prod_date': self.prod_date,


        }