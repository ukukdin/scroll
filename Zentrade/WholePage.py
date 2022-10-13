import time
from bs4 import BeautifulSoup as BS
import requests
from Crawling.common.lib_request import RequestHit
from index_zentrade import zen_lib_es

from Zentrade.libara.zen_data import DataZenProduct
import os
session = requests.Session()
class Whole_list(RequestHit):
    def __init__(self):
        super(Whole_list, self).__init__()
        self.abc = zen_lib_es.DataMallProdList

        self.login_url = "https://www.zentrade.co.kr/shop/member/login_ok.php"
        self.login_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Cookie": " zent_login_id=hitrend; PHPSESSID=12efce5a2457f686a5ac4fc32496e07d; shop_authenticate=Y; cookie_check=0; zent_main_search_skey=b.goodsno; gd_user_enamooPass=XXdndUlRb2NNUmVyRVBJck09My5JUyx0SmdZK01oRy5FdlUxSWRyOw%3D%3D; Xtime=1665635370;",
            "Host": "www.zentrade.co.kr",
            "Referer": "https://www.zentrade.co.kr/shop/member/login_ok.php",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        }
        # 전체상품
        self.Whole_prod_url = "https://www.zentrade.co.kr/shop/goods/goods_list.php?&page="
        self.Whole_prod_url_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
                      "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            "Content-Length": "77",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "gd_user_enamooPass=XXdndUlRb2NNUmVyRVBJck09My5JUyx0SmdZK01ST3dFQGd1SWRyOw%3D%3D; PHPSESSID=218aaf32635ad45cabd4811c93bf84d5; cookie_check=0; zent_main_search_skey=b.goodsno; shop_authenticate=Y; todayGoodsIdx=4269%2C2885%2C; todayGoods=a%3A2%3A%7Bi%3A0%3Ba%3A4%3A%7Bs%3A7%3A%22goodsno%22%3Bs%3A4%3A%224269%22%3Bs%3A7%3A%22goodsnm%22%3Bs%3A31%3A%22%BD%C3%BD%BA%B8%C6%BD%BA+%B3%D7%BF%C0+%B5%A5%BD%BA%C5%A9+%BF%C0%B0%C5%B3%AA%C0%CC%C0%FA%22%3Bs%3A5%3A%22price%22%3Bs%3A5%3A%2212150%22%3Bs%3A3%3A%22img%22%3Bs%3A66%3A%22http%3A%2F%2Fzentrade.hgodo.com%2Fproductimgs%2F4269%2F4269_neo_listimg_01.jpg%22%3B%7Di%3A1%3Ba%3A4%3A%7Bs%3A7%3A%22goodsno%22%3Bs%3A4%3A%222885%22%3Bs%3A7%3A%22goodsnm%22%3Bs%3A21%3A%22%C4%C4%C6%DB%BD%BA+%B0%A2%B5%B5%B1%E2+%C0%DA+%BC%BC%C6%AE%22%3Bs%3A5%3A%22price%22%3Bs%3A4%3A%223650%22%3Bs%3A3%3A%22img%22%3Bs%3A73%3A%22http%3A%2F%2Fzentrade.hgodo.com%2Fproductimgs%2F2885%2F2885_compassset_listimg_01.jpg%22%3B%7D%7D; Xtime=1665554313",
            "Host": "www.zentrade.co.kr",
            'Referer': 'https://www.zentrade.co.kr/shop/goods/goods_list.php?&',
            "Origin": "http://zentrade.co.kr",
            "Upgrade-Insecure-Requests": "1",
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 106.0.0.0 Safari / 537.36'
        }



        self.gubun = 'mall'
        self.path = 'product'
        self.exp_html = '.html'
        # 몰 코드
        self.code_mall = 'M0000001'
        self.name_mall = 'zentrade'
        self.name_code_mall = 'ZEN'

        self.fpath_prodlist = None
        self.flist_prodlist = None
        # 상품 코드
        self.code_prod_hit = 1000000
        self.code_prod_origin = 1000000
        # Data - file
        self.date = None

        self.info = {
            "m_id": "hitrend",
            "password": "!qaz2wsx3edc"
        }
        self.mall_category = {
            '001':'문구/사무용품',
            '004':'생활용품',
            '005':'주방/욕실용품',
            '007':'디지털/자동차',
            '009':'여행/캠핑/취미',
            '011':'패션/이미용/건강',
            '012':'유아동/출산',
        }


        self.login_res = session.post(self.login_url, self.info,self.login_header)

    def setDate(self, date):
        self.date = date

    # 폴더 생성
    def make_directory(self):
        os.chdir("D:/data/")
        if os.path.isdir("D:/data/zentrade"):
            pass
        else:
            os.mkdir("zentrade")
    # 파일 만들어서 저장
    def file_write(self):
        for page in range(52):
            page = page+1
            url = self.Whole_prod_url+str(page)
            login_res = session.get(url).text
            self.make_directory()
            html_file = open(f'./zentrade/'+self.name_mall+'_'+self.name_code_mall+'_'+self.code_mall+'_'+str(page)+'.html','w', encoding='cp949')
            html_file.write(login_res)
            html_file.close()

    # 페이지 상세 정보 가져오기
    def parser_wholelist(self):
        listproduct = []
    
        for page in range(52):
            page =page+1
            file = open(f'd:/data/zentrade/'+self.name_mall+'_'+self.name_code_mall+'_'+self.code_mall+'_'+str(page)+'.html','r', encoding='cp949')
            html = BS(file.read(),'html.parser')

            # html = BS(read.text, "html.parser")
            tag_table = html.select('td[width="25%"]')
            # print(tag_table)
            for productList in tag_table:
                tt = productList.select('div')
                # 숫자
                prod_num = tt[2].string.replace("No. ", "")

                # 상품명
                prod_name = tt[3].string
                ttt = productList.select('b')

                # 상품가격
                prod_price = ttt[0].string

                listproduct.append([prod_num]+[prod_name]+[prod_price])

        #
        # for i in listproduct:
        #     a=i[:][0]
        #


        return listproduct
# a=Whole_list()
# # #파일 생성
# a.file_write()
#
# a.parser_wholelist()
# # 만든 파일 읽어오기
# a.parser_wholelist()


if __name__ =='__main__':
    # test = 'create_file'
    test = 'search_name'
    code_mall="M0000001"
    mall = Whole_list()

    mall.close_session()

    if test == 'create_file':
        mall.parser_wholelist()

    if test == 'search_name':
        malle = zen_lib_es.DataMallProdList()
        mall_code_res = malle.search_prod_num()
        print('mall_code : ', mall_code_res)
        all_data = malle.result_one_data1(mall_code_res)

        for it in all_data:
            print(it.get_data_dict1())
        print('len : ', len(all_data))