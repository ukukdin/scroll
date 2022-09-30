# -*- coding: utf-8 -*-

import time
from bs4 import BeautifulSoup

from common.lib_request import RequestHit
import common.util_fileloader as fl
import common.util_common as cu
from mall.lib.data_prodlist import DataMallProdlist
import random

class Oasismall(RequestHit):

    def __init__(self):
        super(Oasismall, self).__init__()

        # 몰 코드
        self.code_mall = 'M0000001'
        self.name_mall = '오아시스몰'
        self.name_code_mall = 'OASIS'

        # class
        self.malles = DataMallProdlistES()

        # random
        self.rand_sleep_time = random.randint(5, 10)

        # file
        self.gubun = 'mall'
        self.path = 'product'
        self.exp_html = '.html'

        self.fpath_prodlist = None
        self.flist_prodlist = None

        # Data - file
        self.date = None

        # Page
        # 페이지 당 갯수
        self.PAGE = 30
        # 전체 코드별 page 갯수
        self.code_page_dic = {}


        # 입점일
        self.in_date = cu.getDateToday()
        
        # 상품 코드
        self.code_prod_hit = 1000000
        self.code_prod_origin = 1000000

        # URL
        self.mall_url = 'http://www.oasismall.co.kr'
        self.prodlist_page_url = 'http://oasismall.co.kr/shop/shopbrand.html?xcode={}&type=X'
        self.mall_code_page_url = 'http://oasismall.co.kr/shop/shopbrand.html?page={}&xcode={}&mcode=&scode=&type=X&search=&sort=order'
        self.prodlist_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "order_keyword=search.shopping.naver.com%7C%7C202109081051; ____MSLOG__initkey=0.024366545493315517; dgg_default_language=Y; db=WRhBqlLBGdNVtbTP5w9L5YNSTDczTQKqQ9ztePlxz%2BnyZaz0seINN5QfilQyItbYaxbllkW%2BcEelAxTofoSaaWuNR0xRRuTdo9EN0ybv%2F3OezAOlwKcVGET5FjhXOPGE; shop_language=kor; MakeshopLogUniqueId=3e07e0d64009971e4d3be67dd4c351a1; disname=0; ____MSLOG__initday=20210909; psm3086lastdate=202109091542; psm3086inner_ad_cookie=YTozOntzOjM6InJlZiI7czowOiIiO3M6NjoiZGV2aWNlIjtzOjE6InciO3M6Nzoidmlld2NudCI7aTowO30%3D; psm3086searchcookie_2=YTo3OntzOjY6ImRvbWFpbiI7czowOiIiO3M6OToiYWRrZXl3b3JkIjtzOjA6IiI7czoyOiJhZCI7czowOiIiO3M6MTI6InNlYXJjaGVuZ2luZSI7czowOiIiO3M6MTA6InByb2R1Y3RfaWQiO2k6MDtzOjExOiJhZF9jYXRlZ29yeSI7czo2OiJESVJFQ1QiO3M6NjoiaW5pdG9rIjtiOjA7fQ%3D%3D; psm3086ad=eyJhZCI6eyJjYXQiOm51bGwsImF0IjoiRElSRUNUIiwiZCI6Im9hc2lzbWFsbC5jby5rciIsImt3ZCI6bnVsbCwic2UiOm51bGwsInBpZCI6bnVsbCwidCI6MH0sImwiOltdLCJmc3QiOnsiY2F0IjpudWxsLCJhdCI6IkRJUkVDVCIsImQiOiJvYXNpc21hbGwuY28ua3IiLCJrd2QiOm51bGwsInNlIjpudWxsLCJwaWQiOm51bGwsInQiOjB9fQ%3D%3D; psm3086mkt=eyJhZCI6eyJjIjoiRElSRUNUIiwiaW4iOm51bGwsInQiOjB9LCJsIjpbXSwiZnN0Ijp7ImMiOiJESVJFQ1QiLCJpbiI6bnVsbCwidCI6MH19; psm3086visitcnt=2; psm3086initdate=202109091542; psm3086ip_check=0.2481363036147568; viewproduct=%2C002003000035%2C001001000005%2C; psm3086ipr=eyJwIjoiMTQ0MDkwIiwidHMiOjAsInByIjpbIiIsIiIsWyIiLCIiLCIiXV0sImluZiI6WyJzaG9wYnJhbmQiLFsiMDAyIiwiMDAzIiwiIl0sIiJdfQ%3D%3D; basketlinkurl=001; wcs_bt=s_850f64736f8:1631171524; psm3086vss=eyJ0IjoxNjMxMTY5NzIzLCJ1IjoiIiwiZHRoIjo1NSwiayI6ImE2OTRiN2JkODg2MGRkNGRmZWE5YmQwMWIyODQwY2EyIn0%3D; psm3086_spt=1631171524; psm3086svisit=202109091612",
            "Host": "oasismall.co.kr",
            "Referer": "http://oasismall.co.kr/shop/shopbrand.html?xcode=001&type=X&mcode=002",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}

        self.mall_all_code = {"001": "음료",
                      "002": "라면",
                      "003": "과자",
                      "004": "즉석/냉장/냉동식품",
                      "005": "자판기커피/국산차",
                      "006": "간식거리",
                      "007": "기타소모품",
                      "008": "업종별코더"
                      }

    def close_sess_es(self):
        self.sess.close()
        self.malles.closeConnectES()

    # 파일에 들어갈 날짜
    def setDate(self, date):
        self.date = date

    # 상품리스트 파일 생성
    # 전체 코드별 페이지들 상품리스트 파일 생성
    def get_prodlist(self):
        for code, val in self.mall_all_code.items():
            # url
            tmp_url = self.prodlist_page_url.format(code)
            print('tmp_url : ', tmp_url)

            # get page : 코드별 페이지 갯수를 미리 확인한다.
            pages = self.request_page_count(tmp_url)
            time.sleep(self.rand_sleep_time)

            # create file : prodlist html of page
            for page in range(pages):
                # request, create file
                self.getData(code, page+1)
                time.sleep(self.rand_sleep_time)


    # 코드별 페이지 반환
    # 코드별 페이지를 얻기 위한 request/parsor
    def request_page_count(self, url):
        resp = self.request_get(url, self.prodlist_header)
        resp.encoding = 'euc-kr'

        # parsor
        total = None
        soup = cu.setBeautifulSoupParserNoText(resp.text)
        if soup is not None:
            table = soup.findAll('table', width='810')[3]
            if table is not None:
                border = table.findAll('td')[4]
                if border is not None:
                    total = border.find('b').text
                    print(total)

        total = int(total)
        page = total//self.PAGE + 1
        print(page)
        return page


    # Request URL, 코드별 각 페이지의 상품리스트 html 파일을 저장한다.
    def getData(self, code, page):
        # url
        tmp_url = self.mall_code_page_url.format(page, code)
        print(tmp_url)

        # request
        resp = self.request_get(tmp_url, self.prodlist_header)
        resp.encoding = 'euc-kr'
        print(resp.status_code)
        # print(resp.text)

        # create file
        self.createCategoryFile(resp, code, page)

    # CREATE : 상품리스트 Html file
    def createCategoryFile(self, resp, code, page):
        fnam = self.name_code_mall +'_'+ str(code) + '_' + str(page)
        fl.createTodayOpenFile(resp.text, self.gubun, self.path, fnam, self.exp_html)

    #############################################
    # 전체 파일 리스트 가져오기
    def insert_prodlist_es(self):
        # GET ALL : Oasis, prodlist - html
        self.fpath_prodlist, self.flist_prodlist = fl.getDirAllFileList(self.gubun, self.path)
        print('total : ', len(self.flist_prodlist))

        for num, fit in enumerate(self.flist_prodlist):
            print('name : ', fit)
            # read : file name
            readdat = fl.readFileName(self.fpath_prodlist, fit)
            soup = BeautifulSoup(readdat, 'lxml')

            # parsor - 파일의 모든 상품 data class
            file_prod_list = self.parser_prodlist(fit, soup)
            self.malles.insertProdlistES(file_prod_list)

    # parsor : 파일명별로
    def parser_prodlist(self, filename, soup):
        file_prod_list = []

        # parsor : 파일별 데이터
        prod_table = soup.findAll('table', class_='product_table')
        # print(len(prod_table))
        for it in prod_table:
            # parsor
            file_prod_list.append(self.parsor_one_prod(filename, it))
        return file_prod_list


    def parsor_one_prod(self, filename, dat):
        # class data
        mall_data = DataMallProdlist()

        # init
        # timestamp
        timestamp = cu.kst_time()

        # Prod List : 6
        # 1. 몰 code : self.mall_code
        code_mall = ''
        # 2. 몰 name : self.mall_name
        name_mall = ''
        # 3. 몰 name code : self.mall_name_code
        mall_name_code = ''
        # 4. 상품 분류 코드
        ctg_code = ''
        # 상품 분류 코드 페이지
        ctg_page = ''
        # 5. 상품 분류명
        ctg_name = ''
        # 6. 상품리스트 URL
        prodlist_url = ''


        # 1. hit 상품 code : self.code_prod_hit
        hit_prod_code = ''
        # 2. 몰 상품 code : self.code_prod_origin
        mall_prod_code = ''
        # 3. 상품명
        brandname = ''
        # 4. 상품가격
        prod_price = 0
        # 5. 상품상태
        brandname_sta = ''
        # 6. 입점일
        in_date = cu.getDateToday()
        # 7. main image
        main_image = ''
        # 8. 상품 상세 경로
        detail_url = ''
        # 9. 상품갯수
        prod_unit = ''

        # 상품별 파싱
        if dat is not None:
            ############################
            # set prod list : 6
            ############################
            # timestamp
            timestamp = cu.kst_time()

            # Prod List : 6
            # 1. 몰 code : self.mall_code
            code_mall = self.code_mall
            # 2. 몰 name : self.mall_name
            name_mall = self.name_mall
            # 3. 몰 name code : self.mall_name_code
            mall_name_code = self.name_code_mall

            # 4., 5. file name - split
            file_split = filename.split('_')
            if file_split is not None:
                # 4. 상품 분류 코드
                ctg_code = file_split[1].strip()
                # 5. 상품 분류명
                ctg_name = self.mall_all_code[ctg_code]
                ctg_page = file_split[2].strip()
                # print(ctg_code)
                # print(ctg_name)
                # print(ctg_page)
            # 6. 상품리스트 URL
            prodlist_url = self.mall_code_page_url.format(ctg_page, ctg_code)


            #############################
            # Parsor Production : 9
            #############################
            # 1. hit 상품 code : self.hit_prod_code
            hit_prod_code = self.code_prod_hit
            # 2. 몰 상품 code : self.mall_prod_code
            mall_prod_code = self.code_prod_origin

            # PARSOR
            # TR - all
            prod_tr = dat.findAll('tr')

            # 7. 8. 상세페이지 경로 / main image - tr
            detail_url_html = prod_tr[1]
            if detail_url_html is not None:
                # 7. main image
                main_image = self.mall_url + cu.getImageUrl(detail_url_html)
                print(main_image)

                # 8. 상품 상세 경로
                detail_url = self.mall_url + cu.getDetailProdUrl(detail_url_html)
                print(detail_url)

            # 상품명 - tr : 3
            prod_name_html = prod_tr[3]
            if prod_name_html is not None:
                # 3. 상품명
                prod_name_a_html = prod_name_html.find('a')
                # print(prod_name_a_html)
                if prod_name_a_html is not None:
                    brandname = prod_name_a_html.find('font', class_='brandbrandname').text
                    print('brandname : ', brandname)

                # 5. 상품상태
                brandname_sta = prod_name_html.find('font', color='red')
                if brandname_sta is not None:
                    brandname_sta = brandname_sta.text
                    brandname_sta = brandname_sta.replace('(', '')
                    brandname_sta = brandname_sta.replace(')', '')

                else:
                    brandname_sta = '정상판매'
                print(brandname_sta)

            # 4. 상품가격 - tr : 4
            prod_price_html = prod_tr[4]
            if prod_price_html is not None:
                prod_price = prod_price_html.find('span', class_='mk_price').text
                prod_price = prod_price.replace(',', '')
                prod_price = prod_price.replace('원', '')
                prod_price = prod_price.replace('(기본가)', '')
                print(prod_price)

            # 6. 입점일
            in_date = cu.getDateToday()
            # 9. 상품갯수
            # prod_unit = brandname.split('[')[1]
            # prod_unit = prod_unit.replace(']', '')
            # print('prod_unit : ', prod_unit)
            #######################################
            # set data class
            #######################################
            # timestamp
            mall_data.timestamp = timestamp

            # Prod List : 6
            # 1. 몰 code
            mall_data.code_mall = code_mall
            # 2. 몰 name
            mall_data.name_mall = name_mall
            # 3. 몰 name code
            mall_data.name_code_mall = mall_name_code
            # 4. 상품 분류 코드
            mall_data.prod_category = ctg_code
            # 5. 상품 분류명
            mall_data.prod_category_name = ctg_name
            # 6. 상품리스트 URL
            mall_data.prodlist_url = prodlist_url

            # Production : 9
            # 1. hit 상품 code
            mall_data.code_prod_hit = hit_prod_code
            # 2. 몰 상품 code
            mall_data.code_prod_origin = mall_prod_code
            # 3. 상품명
            mall_data.prod_name = brandname
            # 4. 상품가격
            mall_data.prod_price = prod_price
            # 5. 상품상태 : 정상판매/일시품절/품절
            mall_data.prod_sta = brandname_sta

            # 6. 입점일
            mall_data.in_date = in_date
            # 7. main image
            mall_data.main_image = main_image
            # 8. detail url
            mall_data.detail_url = detail_url
            # 9. 상품개수 unit
            mall_data.prod_unit = prod_unit


            mall_data.set_data_dict()
            tmp_dict = mall_data.get_data_dict()
            print('tmp list : ', tmp_dict)
        return mall_data

    ##############################
    # insert ES
    def insert_bulk_es(self):
        pass

    # search ES, for prodname
    def search_fileaname_es(self, name):
        pass


    #############################
    # test - parsor one file
    def parsor_one_file(self, filename):
        fpath = fl.getFilePath(self.gubun, self.path)
        print(fpath)
        print(filename)
        # read : file name
        readdat = fl.readFileName(fpath, filename)
        soup = BeautifulSoup(readdat, 'lxml')

        # parsor - 파일의 모든 상품 data class
        file_prod_list = self.parser_prodlist(filename, soup)
        self.malles.insertProdlistES(file_prod_list)

if __name__ == '__main__':
    # 오아시스몰
    code_mall = 'M0000001'

    # class
    mall = Oasismall()

    test = 'create_file'
    # test = 'insert'
    # test = 'parsor_one_file'
    # test = 'search'

    if test == 'create_file':
        mall.get_prodlist()

    if test == 'insert':
        date = '20210910'
        mall.insert_prodlist_es()

    if test == 'parsor_one_file':
        filename = 'OASIS_001_1_20210916.html'
        mall.parsor_one_file(filename)

    if test == 'search_name':
        from mall.lib.es_pordlist import DataMallProdlistES
        malles = DataMallProdlistES(code_mall.lower())
        res = malles.getAllProdlist()
        all_data = malles.result_all_data(res)
        # print(all_data)

        for it in all_data:
            print(it.get_data_dict())

    # sess close
    mall.close_session()








