import time
from bs4 import BeautifulSoup as BS
import requests
import os
from WholePage import Whole_list
import Crawling.common.util_common as cu
import New_prod as Np
session = requests.Session()
class Product_List(Whole_list):
    def __init__(self):
        super(Product_List, self).__init__()


        self.login_url = "https://www.zentrade.co.kr/shop/member/login_ok.php"
        self.login_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Cookie": "gd_user_enamooPass=XXdndUlRb2NNUmVyRVBJck09My5JUyx0SmdZK01SU3RFQEF0SWRyOw%3D%3D; PHPSESSID=f46862a48c0eaaee9570d7588dd4559f; cookie_check=0; shop_authenticate=Y; zent_login_id=hitrend; Xtime=1665560567",
            "Host": "www.zentrade.co.kr",
            "Referer": "https://www.zentrade.co.kr/shop/member/login_ok.php",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        }
        self.prodctlist = "https://www.zentrade.co.kr/shop/goods/goods_view.php?goodsno="
        # self.prodctlist_url_header = {
        #      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
        #                "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        #     'Accept-Encoding': 'gzip, deflate, br',
        #     'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        #     'Connection': 'keep-alive',
        #     'Host': 'www.zentrade.co.kr',
        #     "Cookie":"PHPSESSID=f46862a48c0eaaee9570d7588dd4559f; shop_authenticate=Y; zent_login_id=hitrend; cookie_check=0",
        #     'Referer': 'https://www.zentrade.co.kr/shop/goods/goods_list.php?&',
        #     "Origin": "http://zentrade.co.kr",
        #     'Upgrade-Insecure-Requests': '1',
        #     'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 106.0.0.0 Safari / 537.36'
        #     }


        self.info = {
            "m_id": "hitrend",
            "password": "!qaz2wsx3edc"
        }
        self.code_mall = 'M0000005'
        self.name_mall = 'zentrade'
        self.name_code_mall = 'New_Detail_List'

        # 로그인
        self.login_res = session.post(self.login_url, self.info,self.login_header)



    def make_directory(self):
        os.chdir("D:/data/")
        if os.path.isdir("D:/data/new_prod_list"):
            pass
        else:
            os.mkdir("new_prod_list")

    # 파일 만들어서 저장하기
    def file_write(self):
        # 신상품 있을때 값 가져와서 진행
        self.no = self.new_prod = Np.New_List().NP()

        for num in self.no:
            No = num[:][0]
            url = self.prodctlist+str(No)+"&category="
            login_res = session.get(url).text
            self.make_directory()
            html_file = open(f'./new_prod_list/' + self.name_mall + '_' + self.name_code_mall + '_' + self.code_mall + '_' +
                    str(No) + '.html', 'w', encoding='cp949')

            html_file.write(login_res)

            html_file.close()

        return str(No)



    def new_prod_list(self):
        new_prod_detail_list = []


        html_file = open(f'd:/data/new_prod_list/' + self.name_mall + '_' + self.name_code_mall + '_' + self.code_mall + '_'+a.file_write()+'.html', 'r', encoding='cp949')
        html = BS(html_file, "html.parser")
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
            # 원산지/과세여부
            country_tax = detail.select('tr[height="30"] td')

            # 배송디테일
            deli_detail = detail.select('form[name=frmView] table:nth-of-type(2) font')

            # 변동내역
            changelist = detail.select('table[align=center] tr:nth-of-type(2) td')

            # 색상정보
            option = detail.select('select[name^=opt]')
            for o in option:
                option_detail = o.get_text(strip=True).replace("== 옵션선택 ==", "")
            # 원산지
            country = country_tax[0].string
            # 과세여부
            prod_tax = country_tax[1].string.replace('\n','')
            # # 배송디테일
            deli_detail1 = deli_detail[0].string
            deli_detail2 = deli_detail[1].string

            # # 가격
            prod_price = prod_price[0].string
            # 배송비
            deli_price = prod_deli[0].string
            # 카테고리
            category = category[0].string
            # 제목
            prod_name = prod_name[0].string
            # 상품번호
            prod_num = prod_num[1].string
            print(prod_num)
            # 변동내용(변경항목,상세내용,변경일시)
            changedlist = changelist[0].string
            detail_text = changelist[1].string
            change_data = changelist[2].string
            new_prod_detail_list.append([prod_num] + [prod_name] + [category] + [prod_price]+[country]+[prod_tax]+[deli_price][deli_detail1]+[deli_detail2]
                                    +[option_detail]+[changedlist]+[detail_text]+[change_data])

        print(new_prod_detail_list)
        return new_prod_detail_list
#
a= Product_List()
# a.__init__()
# a.file_write()
a.new_prod_list()