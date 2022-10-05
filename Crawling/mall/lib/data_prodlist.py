
class DataMallProdlist:
    def __init__(self):
        # all
        self.data_dict = {}
        self.data_list = []

        # 15
        self.timestamp = None

        # Prod List : 6
        # 몰 code
        self.code_mall = None
        # 몰 name
        self.name_mall = None
        # 몰 name code
        self.name_code_mall = None
        # 상품 분류 코드
        self.prod_category = None
        # 상품 분류명
        self.prod_category_name = None
        # 상품리스트 URL
        self.prodlist_url = None

        # Production : 9
        # hit 상품 code
        self.code_prod_hit = None
        # 몰 상품 code
        self.code_prod_origin = None
        # 상품명
        self.prod_name = None
        # 상품가격
        self.prod_price = None
        # 상품상태 : 정상판매/일시품절/품절
        self.prod_sta = None

        # 입점일
        self.in_date = None
        # main image
        self.main_image = None
        # detail url
        self.detail_url = None
        # 상품개수 unit
        self.prod_unit = None

    #########################
    # all
    #########################
    def get_data_dict(self):
        return self.data_dict

    def set_data_dict(self):
        self.data_dict = {
            '@timestamp': self.timestamp,
            # 6
            # 몰 code
            'code_mall' : self.code_mall,
            # 몰 name
            'name_mall' : self.name_mall,
            # 몰 name code
            'name_code_mall': self.name_code_mall,
            # 상품 분류
            'prod_category' : self.prod_category,
            # 상품 분류명
            'prod_category_name' : self.prod_category_name,
            # 상품리스트 URL
            'prodlist_url' :  self.prodlist_url,

            # 9
            # hit 상품 code
            'code_prod_hit' : self.code_prod_hit,
            # 몰 상품 code
            'code_prod_origin' : self.code_prod_origin,
            # 상품명
            'prod_name' : self.prod_name,
            # 상품가격
            'prod_price' : self.prod_price,
            # 상품상태 : 판매중/일시품절/품절
            'prod_sta' : self.prod_sta,

            # 입점일
            'in_date' : self.in_date,
            # main image
            'main_image' : self.main_image,
            # detail url
            'detail_url' : self.detail_url,
            # 상품갯수
            'prod_unit' : self.prod_unit
        }

