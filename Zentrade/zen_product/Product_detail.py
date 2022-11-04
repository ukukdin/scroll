import requests
import os
from Zentrade.zen_product.data_prodlist_detail import DataProdlist_detail
from bs4 import BeautifulSoup as BS
from Zentrade.index_zentrade.zen_lib_detail import DataMallProddetail
import Crawling.common.util_common as cu




# 전체 상품 디테일
class Product_List():
    # print(p)
    def __init__(self):

        super(Product_List, self).__init__()
        self.session = requests.Session()
        self.login_url = "https://www.zentrade.co.kr/shop/member/login_ok.php"
        self.login_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Cookie":'PHPSESSID=912af5bb1da9af6e54dd0871a23d5d8f; shop_authenticate=Y; zent_login_id=hitrend;',
            "Host": "www.zentrade.co.kr",
            "Referer": "https://www.zentrade.co.kr/shop/member/login_ok.php",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        }
        self.prod_detail_url = "https://www.zentrade.co.kr/shop/goods/goods_view.php?goodsno="
        self.prodctlist_url_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
                      "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Host': 'www.zentrade.co.kr',
            "Cookie": 'PHPSESSID=912af5bb1da9af6e54dd0871a23d5d8f; shop_authenticate=Y; zent_login_id=hitrend;',
            'Referer': 'https://www.zentrade.co.kr/shop/goods/goods_list.php?&',
            "Origin": "http://zentrade.co.kr",
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 106.0.0.0 Safari / 537.36'
        }

        self.info = {
            "m_id": "hitrend",
            "password": "!qaz2wsx3edc"
        }
        self.code_mall = 'M0000002'
        self.name_mall = 'zentrade'
        self.name_code_mall = 'Detail_List'

        # 로그인

        self.login_res = self.session.post(self.login_url, self.info,self.login_header)


    def make_directory(self):
        os.chdir("D:/data/")
        if os.path.isdir("D:/data/prod_list"):
            pass
        else:
            os.mkdir("prod_list")

    # 파일 만들어서 저장하기
    def file_write(self):
        import Zentrade.zen_product.Product_list as wholepage
        self.no = wholepage.Whole_list().parser_wholelist()
        # print(self.no)
        for num in self.no:
            self.No=list(num.values())[4]
            # print(self.No)
            url = self.prod_detail_url+str(self.No)+"&category="
            login_res = self.session.get(url,headers=self.prodctlist_url_header).text
            self.make_directory()
            html_file = open(f'./prod_list/' + self.name_mall + '_' + self.name_code_mall + '_' + self.code_mall + '_' +
                             str(self.No) + '.html', 'w', encoding='cp949')

            html_file.write(login_res)

            html_file.close()

        return str(self.No)



    def prod_list(self):

        prod_detail_list = []
        mall = DataProdlist_detail()
        import Zentrade.zen_product.Product_list as wholepage
        nob = wholepage.Whole_list().parser_wholelist()
        for num in nob:
            self.No = list(num.values())[4]
            # print(list(num.values()))
            # 파일 꺼내오기
            html = self.file_open()
            itemlist = html.select("div[class=indiv]")
            for detail in itemlist:
                # 카테고리
                category = detail.select("div[align=right] a")
                # 제목/상품번호
                prod_name = detail.select("td font[style^=font-size] b")
                prod_num = detail.select('td font[style^=font-size] b ')

                # 가격
                prod_price = detail.select('span[id=price]')

                # 배송비
                prod_deli = detail.select('tr[height="20"] b')

                # 원산지/과세여부
                country_tax = detail.select('tr[height="30"] td')

                # 배송디테일
                deli_detail = detail.select('form[name=frmView] table:nth-of-type(2) font')
                changelist = detail.select('table[align=center] tr:nth-of-type(2) td')
                # 변동내역

                # # 옵션정보
                # option1 = detail.findAll('table',attrs={'border':'0','cellpadding':'0','cellspacing':'0','class':'top'})
                #
                # for option2 in option1:
                #      option_detail = option2.get_text(strip=True).replace("== 옵션선택 ==", "")
                #
                #      option= option2.replace('색상 :','')

                # 원산지
                country = country_tax[0].string
                # 과세여부
                prod_tax = country_tax[1].string.replace('\n', '')
                # # 배송디테일
                deli_detail1 = deli_detail[0].string
                deli_detail2 = deli_detail[1].string

                # # 가격
                prod_price = prod_price[0].string.replace(",", '')

                # 배송비
                deli_price = prod_deli[0].string.replace(",", '')

                # 카테고리
                category = category[0].string
                # 제목
                prod_name = prod_name[0].string
                # 상품번호
                prod_num = prod_num[1].string.replace("상품번호 : ", "")
                # print(prod_num)
                # 변동내용(변경항목,상세내용,변경일시)
                changedlist = changelist[0].string
                detail_text = changelist[1].string
                change_date = changelist[2].string

                self.mall_list(category, change_date, changedlist, country, deli_detail1, deli_detail2, deli_price,
                               detail_text, mall, prod_name, prod_num, prod_price, prod_tax)
                tmp_dict = mall.get_date_dict()


                prod_detail_list.append(tmp_dict)

        return prod_detail_list

    def file_open(self):
        html_file = open(
            f'd:/data/prod_list/' + self.name_mall + '_' + self.name_code_mall + '_' + self.code_mall + '_' +
            str(self.No) + '.html', 'r', encoding='cp949')
        html = BS(html_file, "html.parser")
        return html

    def mall_list(self, category, change_date, changedlist, country, deli_detail1, deli_detail2, deli_price,
                  detail_text, mall, prod_name, prod_num, prod_price, prod_tax):
        mall.timestamp = cu.getDateToday()
        mall.code_mall = self.code_mall
        mall.name_mall = self.name_mall
        mall.name_code_mall = self.name_code_mall
        mall.prod_detail_url = self.prod_detail_url + str(self.No) + "&category="
        mall.category = category
        mall.prod_num = prod_num
        mall.prod_name = prod_name
        mall.prod_price = prod_price
        mall.country = country
        mall.prod_tax = prod_tax
        mall.deli_price = deli_price
        mall.deli_detail1 = deli_detail1
        mall.deli_detail2 = deli_detail2
        mall.changedlist = changedlist
        mall.detail_tax = detail_text
        mall.change_dete = change_date
        mall.set_date_dict()


#
a=Product_List()

# # a.file_write()
a.prod_list()
#
# if __name__ == '__main__':
#     # insert
#     test = 'insert'
#     # 검색
#     # test = 'search'
#
#     # test = 'search_all'
#     # login
#     # test = 'login'
#     # create 파일 생성
#     # test = 'createfile'
#
#     detail= Product_List()
#     # -------------------------#
#     # 코드명
#     code_mall = detail.code_mall
#     # 상품명
#     name = '휴지'
#     indexname = 'product_detail'
#     # if test =='login':
#     #     detail.mall_login()
#     # # 파일생성
#     if test == 'createfile':
#         print("하나씩")
#         detail.prod_list()
#
#     # insert
#     if test == 'insert':
#         mall = DataProdlist_detail()
#         DataMallProddetail().insertbulk_prod(Product_List().prod_list(),indexname)
#
#     # code_mall 하나로 검색하는방법
#     if test == 'search':
#         malles = DataMallProddetail()
#
#         mall_code_res = malles.search_mall_code(code_mall,indexname)
#         print('mall_code : ', mall_code_res)
#         all_data = malles.result_all_productdetail(mall_code_res)
#         for it in all_data:
#             print(it.get_date_dict())
#         print('len : ', len(all_data))
#
#     # 전체 검색
#     if test == 'search_all':
#         malles = DataMallProddetail()
#         malles_search_all = malles.getAllProddetail(indexname)
#         print('mall_code : ', malles_search_all)
#         all_data = malles.result_all_productdetail(malles_search_all)
#         for it in all_data:
#             print(it.get_date_dict())
#         print('len : ', len(all_data))
