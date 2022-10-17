# -*- coding: utf-8 -*-

import time
from bs4 import BeautifulSoup

from Crawling.common.lib_request import RequestHit
import Crawling.common.util_fileloader as fl
import Crawling.common.util_common as cu
from Crawling.mall.lib.data_prodlist import DataMallProdlist
from Crawling.mall.lib.es_pordlist import DataMallProdlistES
import random

class Chaesiknara(RequestHit):
    def __init__(self):
        super(Chaesiknara, self).__init__()

        # 몰 코드
        self.code_mall = 'M0000002'
        self.name_mall = '채식나라'
        self.name_code_mall = 'CHAES'

        # class
        self.malles = DataMallProdlistES()

        # random
        self.rand_sleep_time = random.randint(5, 10)

        # 계정
        self.info = {
            "m_id": "",
            "x": "34",
            "y": "17",
            "password": ""
        }

        self.gubun = 'mall'
        self.path = 'product'
        self.exp_html = '.html'

        self.fpath_prodlist = None
        self.flist_prodlist = None

        # Data - file
        self.date = None

        # Page
        # 페이지 당 상품 개수가 늘어남 : 페이지 없음
        # 페이지 당 갯수
        # self.PAGE = 30
        # 전체 코드별 page 갯수
        # self.code_page_dic = {}


        # 입점일
        self.in_date = cu.getDateMonth()

        # 상품 코드
        self.code_prod_hit = 1000000
        self.code_prod_origin = 1000000

        # URL
        self.mall_url = 'http://chaesiknara.co.kr'
        self.login_url = 'http://chaesiknara.co.kr/shop/member/login_ok.php'
        self.login_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Length": "77",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "PHPSESSID=ufnrduk8m51c6fudjg2vapelo5; godoLog=20221013; shop_authenticate=Y; cookie_check=0; Xtime=1665636356; wcs_bt=s_29f5659006d8:1665636357",
            "Host": "chaesiknara.co.kr",
            "Origin": "http://chaesiknara.co.kr",
            "Referer": "http://chaesiknara.co.kr/shop/member/login.php?&",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        }

        self.prodlist_url = 'http://chaesiknara.co.kr/shop/goods/goods_list.php?&category={}'
        self.prodlist_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "zent_login_id=hitrend; PHPSESSID=12efce5a2457f686a5ac4fc32496e07d; shop_authenticate=Y; zent_main_search_skey=b.goodsno; gd_user_enamooPass=XXdndUlRb2NNUmVyRVBJck09My5JUyx0SmdZK01oRy5FdlUxSWRyOw%3D%3D; todayGoodsIdx=4269%2C4263%2C4264%2C13%2C924%2C2464%2C4268%2C4267%2C; todayGoods=a%3A8%3A%7Bi%3A0%3Ba%3A4%3A%7Bs%3A7%3A%22goodsno%22%3Bs%3A4%3A%224269%22%3Bs%3A7%3A%22goodsnm%22%3Bs%3A31%3A%22%BD%C3%BD%BA%B8%C6%BD%BA+%B3%D7%BF%C0+%B5%A5%BD%BA%C5%A9+%BF%C0%B0%C5%B3%AA%C0%CC%C0%FA%22%3Bs%3A5%3A%22price%22%3Bs%3A5%3A%2212150%22%3Bs%3A3%3A%22img%22%3Bs%3A66%3A%22http%3A%2F%2Fzentrade.hgodo.com%2Fproductimgs%2F4269%2F4269_neo_listimg_01.jpg%22%3B%7Di%3A1%3Ba%3A4%3A%7Bs%3A7%3A%22goodsno%22%3Bs%3A4%3A%224263%22%3Bs%3A7%3A%22goodsnm%22%3Bs%3A24%3A%22%C4%BF%C7%C3%B8%B5+%BD%CA%C0%DA%B0%A1%B7%CE+%BC%F6%B5%B5%B2%C0%C1%F6%22%3Bs%3A5%3A%22price%22%3Bs%3A4%3A%226840%22%3Bs%3A3%3A%22img%22%3Bs%3A69%3A%22http%3A%2F%2Fzentrade.hgodo.com%2Fproductimgs%2F4263%2F4263_faucet_listimg_01.jpg%22%3B%7Di%3A2%3Ba%3A4%3A%7Bs%3A7%3A%22goodsno%22%3Bs%3A4%3A%224264%22%3Bs%3A7%3A%22goodsnm%22%3Bs%3A20%3A%224P+%B8%B6%C5%B0+%B0%E8%B7%AE%BD%BA%C7%AC%BC%BC%C6%AE%22%3Bs%3A5%3A%22price%22%3Bs%3A4%3A%221880%22%3Bs%3A3%3A%22img%22%3Bs%3A78%3A%22http%3A%2F%2Fzentrade.hgodo.com%2Fproductimgs%2F4264%2F4264_measuring_spoon_listimg_01.jpg%22%3B%7Di%3A3%3Ba%3A4%3A%7Bs%3A7%3A%22goodsno%22%3Bs%3A2%3A%2213%22%3Bs%3A7%3A%22goodsnm%22%3Bs%3A13%3A%22%BE%C8%C5%D7%B3%AA+%C8%BF%C0%DA%BC%D5%22%3Bs%3A5%3A%22price%22%3Bs%3A4%3A%221310%22%3Bs%3A3%3A%22img%22%3Bs%3A70%3A%22http%3A%2F%2Fzentrade.hgodo.com%2Fproductimgs%2F13%2F13_antennaback_listimg_01.jpg%22%3B%7Di%3A4%3Ba%3A4%3A%7Bs%3A7%3A%22goodsno%22%3Bs%3A3%3A%22924%22%3Bs%3A7%3A%22goodsnm%22%3Bs%3A24%3A%22ZSM+%C0%AF%B7%E1%B9%F6%C0%FC+30%C0%CF+%C0%CC%BF%EB%B1%C7%22%3Bs%3A5%3A%22price%22%3Bs%3A5%3A%2255000%22%3Bs%3A3%3A%22img%22%3Bs%3A19%3A%221589269100547s0.jpg%22%3B%7Di%3A5%3Ba%3A4%3A%7Bs%3A7%3A%22goodsno%22%3Bs%3A4%3A%222464%22%3Bs%3A7%3A%22goodsnm%22%3Bs%3A32%3A%22%C4%C3%B7%AF+%C0%DA%B9%D9%B6%F3+%B9%CC%B4%CF+%BD%BA%B8%B6%C6%AE%C6%F9+%BB%EF%B0%A2%B4%EB%22%3Bs%3A5%3A%22price%22%3Bs%3A4%3A%221790%22%3Bs%3A3%3A%22img%22%3Bs%3A69%3A%22http%3A%2F%2Fzentrade.hgodo.com%2Fproductimgs%2F2464%2F2464_tripod_listimg_01.jpg%22%3B%7Di%3A6%3Ba%3A4%3A%7Bs%3A7%3A%22goodsno%22%3Bs%3A4%3A%224268%22%3Bs%3A7%3A%22goodsnm%22%3Bs%3A17%3A%22%BF%F8%C5%CD%C4%A1+%BC%F6%B5%B5%BF%AC%B0%E1%B1%E2%22%3Bs%3A5%3A%22price%22%3Bs%3A4%3A%224030%22%3Bs%3A3%3A%22img%22%3Bs%3A78%3A%22http%3A%2F%2Fzentrade.hgodo.com%2Fproductimgs%2F4268%2F4268_waterconnection_listimg_01.jpg%22%3B%7Di%3A7%3Ba%3A4%3A%7Bs%3A7%3A%22goodsno%22%3Bs%3A4%3A%224267%22%3Bs%3A7%3A%22goodsnm%22%3Bs%3A17%3A%22%C8%B8%C0%FC%BD%C4+%C8%A3%BD%BA%BF%AC%B0%E1%B1%E2%22%3Bs%3A5%3A%22price%22%3Bs%3A4%3A%221830%22%3Bs%3A3%3A%22img%22%3Bs%3A78%3A%22http%3A%2F%2Fzentrade.hgodo.com%2Fproductimgs%2F4267%2F4267_hose_connection_listimg_01.jpg%22%3B%7D%7D; cookie_check=0; Xtime=1665636816",
            "Host": "chaesiknara.co.kr",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        }
        self.test_header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'PHPSESSID=5oj3pvnscnk5av6d6hqa5vp272; cookie_check=0; godoLog=20220913; shop_authenticate=Y; _fbp=fb.2.1663043152967.954208082; todayGoodsIdx=1880%2C; todayGoods=a%3A1%3A%7Bi%3A0%3Ba%3A4%3A%7Bs%3A7%3A%22goodsno%22%3Bs%3A4%3A%221880%22%3Bs%3A7%3A%22goodsnm%22%3Bs%3A102%3A%22%5B%B3%C3%B5%BF%5D%BA%F1%B0%C7%BD%D2%B1%EE%BD%BA+1.6kg%2880g+X+20%B0%B3%C0%D4%29+%5B%B4%EB%C6%F7%C0%E5%5D%2F+%BA%F1%B0%C7%C4%BF%C6%B2%B7%BF+Vegan+Rice_Cuttlet%2F%BC%D2%C7%B3%B5%B5%BD%C3%B6%F4%2F%C7%D0%BB%FD%B5%B5%BD%C3%B6%F4%B9%DD%C2%F9%22%3Bs%3A5%3A%22price%22%3Bs%3A5%3A%2226000%22%3Bs%3A3%3A%22img%22%3Bs%3A19%3A%221550549212607s0.jpg%22%3B%7D%7D; Xtime=1663045613; wcs_bt=s_29f5659006d8:1663045606',
            'Host': 'chaesiknara.co.kr',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
        }

        self.mall_all_code = {
            '062': '비건아이스크림',
            '047': '식물성콩고기',
            '061': '라면/만두/분식',
            '051': '빵/과자/사탕/음료',
            '050': '농산물/김치/찬/과일',
            '053': '장류/양념/소스/오일',
            '052': '조미료/소금/설탕',
            '054': '건강/뷰티/다이어트',
            '057': '무오신채',
            '055': '생활/주방',
            '033': '비건동물사료'
        }

    def close_sess_es(self):
        self.sess.close()
        self.malles.closeConnectES()

    # 파일에 들어갈 날짜
    def setDate(self, date):
        self.date = date

    #########################
    # request
    #########################
    # login
    def mall_login(self):
        resp = self.request_post_noheader(self.login_url, self.info)
        print(resp.text)

    # Request URL, 코드별 각 페이지의 상품리스트 html 파일을 저장한다.
    def getData(self, code):
        # url
        tmp_url = self.prodlist_url.format(code)

        # request
        resp = self.request_get_noheader(tmp_url)
        # print(resp.text)

        # create file
        self.createCategoryFile(resp, code, 0)


    #########################
    # parser
    #########################
    # parsor : 파일명별로
    def parser_prodlist(self, filename, soup):
        file_prod_list = []

        # parsor : 파일별 데이터
        prod_table = soup.findAll('td', attrs={'align':'center', 'valign': 'top', 'width': '25%', 'style': 'padding-bottom:25px;'})
        print(len(prod_table))

        for num, it in enumerate(prod_table):
            # print(num , ' : ########################' )

            file_prod_list.append(self.parsor_one_prod(filename, it))
        print(file_prod_list)
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
        # 5. 상품상태 : 정상판매/일시품절/품절
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
            prodlist_url = self.prodlist_url.format(ctg_code)

            #############################
            # Parsor Production : 9
            #############################
            # 1. hit 상품 code : self.hit_prod_code
            hit_prod_code = self.code_prod_hit

            # 8, 2, 7
            tmp_div = dat.find('div', style='text-align:center;')
            if tmp_div is not None:
                # print('tmp_div', tmp_div)
                # 8. detail url
                detail_url = self.mall_url + cu.getDetailProdUrl(tmp_div).replace('..', '')
                print('detail_url : ', detail_url)

                # 2. 몰 상품 code : self.mall_prod_code
                mall_prod_code = detail_url.split('?')[1].split('=')[1].split('&')[0]
                print('mall_prod_code : ', mall_prod_code)

                # 7. main image
                main_image = self.mall_url + cu.getImageUrl(tmp_div).replace('..', '')
                print(main_image)

            div_style = dat.find('div', style='padding:10px 0 0 0; text-align:left; width:130px;')
            if div_style is not None:
                # 5. 상품상태
                tmp_div2 = div_style.find('div', style='padding:3px 0;')
                if tmp_div2 is not None:
                    brandname_sta = '품절'
                else:
                    brandname_sta = '정상판매'
                print(brandname_sta)

                # 3. 상품명
                tmp_name = div_style.getText().strip()
                tmp_name = tmp_name.split('\n')
                # print(tmp_name)
                brandname = tmp_name[0]
                print('brandname : ', brandname)

                # 4. 상품가격
                prod_price = tmp_name[1]
                if ' ' in prod_price:
                    prod_price = prod_price.split(' ')[1]
                prod_price = cu.parsorPrice(prod_price)
                print('prod_price : ', prod_price)
            # 6. 입점일
            in_date = cu.getDateToday()
            # 9. 상품갯수
            prod_unit = ''

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


    #############################
    # file
    #############################
    # CREATE : 상품리스트 Html file
    def createCategoryFile(self, resp, code, page):
        if page == 0:
            fnam = self.name_code_mall+'_'+str(code)
        else:
            fnam = self.name_code_mall+'_'+str(code)+'_'+str(page)

        fl.createTodayOpenFile(resp.text, self.gubun, self.path, fnam, self.exp_html)

    # 전체 파일 리스트 가져오기
    def insert_prodlist_es(self):
        # GET ALL : Oasis, prodlist - html
        self.fpath_prodlist, self.flist_prodlist = fl.getDirAllFileList(self.gubun, self.path)
        print('total : ', len(self.flist_prodlist))

        for num, fit in enumerate(self.flist_prodlist):
            # print('name : ', fit)
            # read : file name
            readdat = fl.readFileName(self.fpath_prodlist, fit)
            soup = BeautifulSoup(readdat, 'lxml')

            # parsor - 파일의 모든 상품 data class
            file_prod_list = self.parser_prodlist(fit, soup)
            self.malles.insertProdlistES(file_prod_list)


    #############################
    # function
    #############################
    # 상품리스트 파일 생성
    # 전체 코드별 페이지들 상품리스트 파일 생성
    def get_prodlist(self):
        for code, val in self.mall_all_code.items():
            self.getData(code)
            time.sleep(3)


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

    #######################
    test = 'create_file'
    test = ' login'
    test = 'insert'
    # test = 'search_name'
    # test = 'parsor_one_file'

    #######################
    code_mall = 'M0000002'
    # sta = '정상판매'
    sta = '품절'
    # class
    mall = Chaesiknara()

    #######################
    if test == 'create_file':
        mall.get_prodlist()

    # login
    if test == 'login':
        mall.mall_login()

    # insert
    if test == 'insert':
        filename = 'CHAES_062_20221013.html'
        mall.parsor_one_file(filename)

    if test == 'search_name':
        malles = DataMallProdlistES()
        mall_code_res = malles.search_mall_code(code_mall, sta)
        print('mall_code : ', mall_code_res)
        all_data = malles.result_all_data(mall_code_res)

        for it in all_data:
            print(it.get_data_dict())
        print('len : ', len(all_data))

    #######################
    # sess close
    mall.close_session()