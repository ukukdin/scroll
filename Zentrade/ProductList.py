import time
from bs4 import BeautifulSoup as BS
import requests
from Crawling.common.lib_request import RequestHit
import Crawling.common.util_fileloader as fl
import Crawling.common.util_common as cu
from Crawling.mall.lib.data_prodlist import DataMallProdlist
from Crawling.mall.lib.es_pordlist import DataMallProdlistES
import random
import pandas as pd
import os
from WholePage import Whole_list as wl
import html5lib
session = requests.Session()
class Product_List(wl):
    def __init__(self):
        super(Product_List, self).__init__()


        self.prodctlist = "https://www.zentrade.co.kr/shop/goods/goods_view.php?goodsno="
        self.loginPage = "https://www.zentrade.co.kr/shop/member/login_ok.php"
        self.info = {
            "m_id": "hitrend",
            "password": "!qaz2wsx3edc"
        }
        self.code_mall = 'M0000002'
        self.name_mall = 'zentrade'
        self.name_code_mall = 'Detail_List'
        self.login_res = session.post(self.login_url, self.info, self.login_header)
        # self.h = 'd:/date/zentrade'+self.name_mall+'_'+self.name_code_mall+'_'+self.code_mall+'_10.html'
        # print(self.h)
        # self.file = pd.read_html(self.h,encoding='cp949')


    def make_directory(self):
        os.chdir("D:/data/")
        if os.path.isdir("D:/data/prod_list"):
            pass
        else:
            os.mkdir("prod_list")
    # 파일 만들어서 저장하기
    def file_write(self):
        self.no = wl().parser_wholelist()
        for num in self.no:
            No = num[:][0]
            url = self.prodctlist+str(No)+"&category="
            login_res = session.get(url).text
            self.make_directory()
            html_file = open(f'./prod_list/' + self.name_mall + '_' + self.name_code_mall + '_' + self.code_mall + '_' +
                    str(No) + '.html', 'w', encoding='cp949')
            html_file.write(login_res)
            html_file.close()



    def prod_list(self):
        prod_detail_list = []
        # self.no = wl().parser_wholelist()
        # for num in self.no:
        #     No = num[:][0]
        html_file = open(f'./prod_list/' + self.name_mall + '_' + self.name_code_mall + '_' + self.code_mall + '_' +
                         '4269' + '.html', 'r', encoding='cp949')
        html = BS(html_file.read, "html.parser")
        itemlist = html.select("div[class=indiv]")
        for detail in itemlist:
            # 카테고리
            category = detail.select("div[align=right] a")
            # 제목/상품번호
            prod_name = detail.select("td font[style^=font-size] b")
            prod_num = detail.select('form[name=frmView] table:nth-of-type(2) font')
            # 가격
            prod_price = detail.select('span[id=price]')
            # 배송비
            prod_deli = detail.select('tr[height="20"] b')
            # 배송디테일
            deli_detail = detail.select('tr[height="30"] td')
            # 변동내역
            changelist = detail.select('table[align=center] tr:nth-of-type(2) td')

            # 색상정보
            option = detail.select('select[name^=opt]')
            for o in option:
                option_detail = o.get_text(strip=True).replace("== 옵션선택 ==", "")
                # 원산지
            country = deli_detail[0].string
            # 과세여부
            prod_tax = deli_detail[1].string
            # 배송디테일
            deli_detail = deli_detail[0].string
            deli_detail2 = deli_detail[1].string
            # 가격
            prod_price = prod_price[0].string
            # 배송비
            deli_price = prod_deli[0].string
            # 카테고리
            category = category[0].string
            # 제목
            prod_name = prod_name[0].string
            # 상품번호
            prod_num = prod_num[1].string
            # 변동내용(변경항목,상세내용,변경일시)
            changedlist = changelist[0].string
            detail_text = changelist[1].string
            change_data = changelist[2].string
            prod_detail_list.append([prod_num] + [prod_name] + [category] + [prod_price] +
                                    [country] + [prod_tax] + [deli_price] + [deli_detail] +
                                    [deli_detail2] + [option_detail] + [changedlist] + [detail_text] + [change_data])

        return prod_detail_list
#
a= Product_List()
a.file_write()