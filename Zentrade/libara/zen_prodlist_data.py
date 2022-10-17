# 상세 상품 리스트 + 상세 신상품 리스트
class DataZenProductList:
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
        self.prod_date = None
        # 원산지
        self.country = None

        # 과세여부
        self.prod_tax = None

        # 배송비
        self.deli_price = None

        # 배송 디테일
        self.deli_detail1 = None
        self.deli_detail2 = None

        # 변동내용: 변경항목,상세내용,변경일시
        self.changedlist = None
        self.detail_tax = None
        self.change_dete = None


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
            #상품가격
            'prod_price':self.prod_price,
            'prod_date':self.prod_date,
            # 원산지
            'country': self.country,
            # 과세여부
            'prod_tax':self.prod_tax,
            # 배송비
            'deli_price':self.deli_price,
            # 배송 디테일
            'deli_detail1':self.deli_detail1,
            'deli_detail2': self.deli_detail2,
            # 선택 옵션
            # 'option' : self.option,
            # 변동내용: 변경항목,상세내용,변경일시
            'changedlist':self.changedlist,
            'detail_tax': self.detail_tax,
            'change_dete': self.change_dete


        }