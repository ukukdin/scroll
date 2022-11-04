from bs4 import BeautifulSoup as BS
import requests
from elasticsearch_dsl import Document, Integer, Keyword, connections,Text,Date,Nested

from Crawling.common.lib_request import RequestHit
from Zentrade.zen_product.data_product_list import DataProductList
from Zentrade.index.index_product_list import DataWholepageIndex
from Zentrade.index_zentrade.zen_lib_detail import DataMallProddetail
import Crawling.common.util_common as cu
import os
from Zentrade.zen_product_out.Out_product import out_of_stock


# 전체 상품 페이지 리스트
class Whole_list(RequestHit):
    def __init__(self):
        super(Whole_list, self).__init__()
        self.session = requests.Session()

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
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 106.0.0.0 Safari / 537.36'
        }



        self.gubun = 'zentrade'
        self.path = 'wholepage'
        self.exp_html = '.html'
        # 몰 코드
        self.code_mall = 'M0000001'
        self.name_mall = 'zentrade'
        self.name_code_mall = 'ZEN'

        # 상품 코드
        # Data - file
        self.date = None
        self.info = {
            "return_url": "https://www.zentrade.co.kr/shop/goods/goods_list.php?&page=",
            "m_id": "hitrend",
            "password": "!qaz2wsx3edc"
        }
    # login
    def mall_login(self):
        login_res = self.session.post(self.login_url,self.info)
        print(login_res.text)

    # 폴더 생성
    def make_directory(self):
        os.chdir("D:/data")
        if os.path.isdir("D:/data/"+self.gubun+'/'+self.path):
            pass
        else:
            os.makedirs("./"+self.gubun+'/'+self.path)
            
    # 파일 만들어서 저장
    def file_write(self):
        for page in range(1,52,1):
            url = self.Whole_prod_url+str(page)
            login_res = self.session.get(url).text
            self.make_directory()
            html_file = open(f'./'+self.gubun+'/'+self.path+'/'+self.name_mall+'_'+self.name_code_mall+'_'+self.code_mall+'_'+str(page)+'.html','w', encoding='cp949')
            html_file.write(login_res)
            html_file.close()
        print("완료")

    # 페이지 상세 정보 가져오기
    def parser_wholelist(self):
        listproduct = []
        mall = DataProductList()
        for page in range(1,52,1):

            html = self.file_open(page)
            tag_table = html.select('td[width="25%"]')

            for productList in tag_table:
                tt = productList.select('div')
                # 숫자
                self.prod_num = tt[2].string.replace("No. ", "")

                # 상품명
                prod_name = tt[3].string
                ttt = productList.select('b')

                # 상품가격
                self.mall_list(mall, page, prod_name, ttt)

                mall.set_date_dict()
                tmp_dict = mall.get_date_dict()


                listproduct.append(tmp_dict)
        return listproduct

    def file_open(self, page):
        file = open(
            f'd:/data/' + self.gubun + '/' + self.path + '/' + self.name_mall + '_' + self.name_code_mall + '_' + self.code_mall + '_' + str(
                page) + '.html', 'r', encoding='cp949')
        html = BS(file.read(), 'html.parser')
        return html

    def mall_list(self, mall, page, prod_name, ttt):
        prod_price = ttt[0].string.replace(",", "")
        mall.code_mall = self.code_mall
        mall.name_mall = self.name_mall
        mall.name_code_mall = self.name_code_mall
        mall.prodlist_url = self.Whole_prod_url + str(page)
        mall.prod_num = self.prod_num
        mall.prod_name = prod_name
        mall.prod_price = prod_price

#     def nested(self):
#         dic =[]
#
#         code_mall = 'moodle'
#         name_code_mall = 'zentrade'
#         name_mall = 'zen'
#         prod_name='아프다'
#         prod_num = '12'
#         prod_price = 1234
#         prod_url = 'XXX'
#         dic.append([code_mall,name_code_mall,prod_url,name_mall,
#                    prod_num,prod_name,prod_price])
#         print(dic)
#         return dic

if __name__ == '__main__':

    indexname = 'product_list'

#     #######################
#     # test = 'create_file
#     # test = ' login'
    test = 'insert'
    # test = 'search_name'
    # test = 'search'
    # test = 'parsor_one_file'
    #######################
    name = "시스맥스"
    whole = Whole_list()

    # if test == 'create_file':
    # whole.file_write()
    # # login
    # if test == 'login':
    # whole.mall_login()
    #  mall = whole.code_mall


     # insert
    if test == 'insert' :
        mall = DataMallProddetail()
        a=Whole_list().parser_wholelist()
        from Zentrade.zen_product.Product_detail import Product_List
        b=Product_List().prod_list()
        # b=out_of_stock().outstock()

        DataMallProddetail().insertbulk_prod(a,b,indexname)

#
#     if test == 'search_name':
#         malles = DataMallProddetail()
#         mall_code_res = malles.search_mall_code(mall,indexname)
#         print('mall_code : ', mall_code_res)
#         all_data = malles.result_all_data_product(mall_code_res)
#         for it in all_data:
#             print(it.get_date_dict())
#         print('len : ', len(all_data))
#
#
#
#     # #######################
#     # # sess close
    whole.close_session()

