# 상품 리스트 + 신상품 리스트 + 품절 리스트
class DataZenProduct:
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

        # 상품 카테고리
        self.category = None
        # 상품 번호
        self.prod_num = None
        # 상품명
        self.prod_name = None

        # 상품가격
        self.prod_price = None
        # 신상품 입고 날짜
        self.prod_date = None
        # 재고여부
        self.prod_out = None

        # 품절이유
        self.reason = None

        # 재입고 여부
        self.reorder = None

        # 재입고 예정일
        self.reorder_date = None

        # 삭제예정일
        self.expire_date = None

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
            # 카테고리
            'category':self.category,
            # 상품명
            'prod_num':self.prod_num,
            #상품이름
            'prod_name':self.prod_name,
            # 상품가격
            'prod_price': self.prod_price,
            # 신상품 입고날짜
            'prod_date': self.prod_date,

            #재고여부
            'prod_out': self.prod_out,
            #품절이유
            'reason':self.reason,
            #재입고 여부
            'reorder':self.reorder,
            #재입고 예정일
            'reorder_date':self.reorder_date,
            #삭제예정일
            'expire_date':self.expire_date

        }