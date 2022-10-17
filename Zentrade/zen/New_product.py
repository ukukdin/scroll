import re
import pandas as pd
import requests
import os
from bs4 import BeautifulSoup as BS

import Crawling.common.util_common as cu
from Zentrade.libara.zen_prodlist_data import DataZenProductList
from Zentrade.index_zentrade.zen_lib_newprod import DataMallNewProduct
session = requests.Session()

class New_List():
    def __init__(self):
        super(New_List, self).__init__()
        
        self.zenmall = DataMallNewProduct()
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

        self.new_prod = "https://www.zentrade.co.kr/shop/goods/goods_new.php?searchDate="

        self.info = {
            "m_id": "hitrend",
            "password": "!qaz2wsx3edc"
        }
        self.code_mall = 'M0000004'
        self.name_mall = 'zentrade'
        self.name_code_mall = 'NewProduct'

        self.malles = DataMallNewProduct()


        self.login_res = session.post(self.login_url, self.info, self.login_header)

    def make_directory(self):
        os.chdir("D:/data/")
        if os.path.isdir("D:/data/NewProduct"):
              pass
        else:
            os.mkdir("NewProduct")

    def file_write(self):

        a = self.new_prod+cu.getDateToday()
        login_res = session.get(a).text
        self.make_directory()
        html_file = open(
            f'./NewProduct/' + self.name_mall + '_' + self.name_code_mall + '_' + self.code_mall + '_' +cu.getDateToday()+'.html', 'w', encoding='cp949')
        html_file.write(login_res)
        html_file.close()

    # 새로운 상품이 있으면 파싱 프로세스
    def NP(self):
        new_product_list = []

        file = open(
            f'd:/data/NewProduct/' + self.name_mall + '_' + self.name_code_mall + '_' + self.code_mall + '_'+cu.getDateToday()+'.html', 'r', encoding='cp949')
        self.html = BS(file.read(), "html.parser")
        self.new_list = self.html.findAll("td", attrs={"bgcolor": "FFD9EC", "height": "40", "id": "b_white",
                                               "style": "padding-left:15px;"})
        mall = DataZenProductList()

        for a,i in enumerate(self.new_list):
            num = i.findAll("b")
            # 상품번호
            prod_num = num[1].string
            if prod_num == str(0):
                print("오늘의 신상품은 없습니다.")
            else:
                print("오늘의 신상품은 " + str(prod_num) + "개의 상품이 있습니다.")
                print()
                prod_list = self.html.findAll("td", attrs={'align': 'center', 'valign': 'top', 'width': '25%'})
                for list in prod_list:
                    detail = list.select('div')
                    # 신상품 등록일
                    prod_date = detail[2].string.replace("신상품 등록일 : ", "")
                    print('prod_date 신상품 데이는:' ,prod_date)
                    # 새로운 상품 번호
                    prod_num = detail[3].string.replace("No. ", "")
                    print('prod_num 신상품 데이는:' ,prod_date)

                    # 새로운 상품 이름
                    prod_name = detail[4].string
                    print('prod_name 신상품 데이는:' ,prod_name)

                    p = detail[1].select('b')
                    prod_price = p[0].string.replace(",","")
                    print('prod_price 신상품 데이는:' ,prod_price)

                    mall.timestamp = cu.getDateToday()
                    mall.code_mall = self.code_mall
                    mall.name_mall = self.name_mall
                    mall.name_code_mall=self.name_code_mall
                    mall.category = ''
                    mall.prod_num = prod_num
                    mall.prod_name =prod_name
                    mall.prod_price=prod_price
                    mall.prod_date = prod_date
                    mall.country = ''
                    mall.prod_tax = ''
                    mall.deli_price = ''
                    mall.deli_detail1=''
                    mall.deli_detail2 = ''
                    mall.changedlist=''
                    mall.detail_tax=''
                    mall.change_dete = ''

                    mall.set_date_dict()
                    tmp_dict = mall.get_date_dict()

                    newlist = [i for i in tmp_dict.values()]
                    print(tmp_dict)
                    print()




        return tmp_dict


a = New_List()
# 파일 불러오기
# a.file_write()
# 신상품 있는지 없는지 확인 후 값 가져오는것.


if __name__ =='__main__':


    test  = 'newproductlist'

    if test == 'newproductlist':
        mall = DataZenProductList()
        New_List().NP()
        DataMallNewProduct().insertbulk_newprod(New_List().NP())
