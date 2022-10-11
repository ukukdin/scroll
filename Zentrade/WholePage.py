import time
from bs4 import BeautifulSoup as BS
import requests
from Crawling.common.lib_request import RequestHit
import Crawling.common.util_fileloader as fl
import Crawling.common.util_common as cu
from elasticsearch import Elasticsearch
import random
import os
session = requests.Session()
class Whole_list(RequestHit):
    def __init__(self):
        super(Whole_list, self).__init__()


        self.login_url = "https://www.zentrade.co.kr/shop/member/login_ok.php"
        self.login_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Length": "77",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "PHPSESSID=e9o0rmmdnf76i0ehe7597cf126; cookie_check=0; godoLog=20210916; shop_authenticate=Y; _fbp=fb.2.1631754439491.1397331112; Xtime=1631754469; wcs_bt=s_29f5659006d8:1631754472",
            "Host": "zentrade.co.kr",
            "Origin": "http://zentrade.co.kr",
            "Referer": "http://zentrade.co.kr/shop/member/login.php?&",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        }
        # 전체상품
        self.Whole_prod_url = "https://www.zentrade.co.kr/shop/goods/goods_list.php?&page="
        self.Whole_prod_url_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Length": "77",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "PHPSESSID=e9o0rmmdnf76i0ehe7597cf126; cookie_check=0; godoLog=20210916; shop_authenticate=Y; _fbp=fb.2.1631754439491.1397331112; Xtime=1631754469; wcs_bt=s_29f5659006d8:1631754472",
            "Host": "zentrade.co.kr",
            "Origin": "http://zentrade.co.kr",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
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
                # print(ttt)
                # 상품가격
                prod_price = ttt[0].string

                listproduct.append([prod_num]+[prod_name]+[prod_price])

        #
        # for i in listproduct:
        #     a=i[:][0]
        #


        return listproduct
a=Whole_list()
# #파일 생성
# a.file_write()


# # 만든 파일 읽어오기
a.parser_wholelist()
    # def insertData(self):
    #     es = Elasticsearch('[192.168.0.41]:9200')
    #     index = 'WholePage'
    #
    #     doc = {
    #         "prod_num":
    #     }


if __name__ =='__main__':
    test = 'create_file'

    code_mall="M0000001"
    mall = Whole_list()

    mall.close_session()

    if test == 'create_file':
        mall.parser_wholelist()