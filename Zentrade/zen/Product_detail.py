from bs4 import BeautifulSoup as BS
import requests
import os
from Zentrade.libara.zen_prodlist_detail import DataZenProductList
from bs4 import BeautifulSoup as BS
from Zentrade.index_zentrade.zen_lib_detail import DataMallProddetail
import Crawling.common.util_common as cu


session = requests.Session()


class Product_List():
    # print(p)
    def __init__(self):

        super(Product_List, self).__init__()

        self.login_url = "https://www.zentrade.co.kr/shop/member/login_ok.php"
        self.login_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Cookie":'PHPSESSID=e71bd67e31ee5a8951ee2bed3f31913c; shop_authenticate=Y; zent_login_id=hitrend;',
            "Host": "www.zentrade.co.kr",
            "Referer": "https://www.zentrade.co.kr/shop/member/login_ok.php",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        }
        self.prodctlist = "https://www.zentrade.co.kr/shop/goods/goods_view.php?goodsno="
        self.prodctlist_url_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
                      "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Host': 'www.zentrade.co.kr',
            "Cookie": 'PHPSESSID=e71bd67e31ee5a8951ee2bed3f31913c; shop_authenticate=Y; zent_login_id=hitrend;',
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
    def mall_login(self):
        login_res = session.post(self.login_url, self.info,self.login_header)
        print(login_res.text)

    def make_directory(self):
        os.chdir("D:/data/")
        if os.path.isdir("D:/data/prod_list"):
            pass
        else:
            os.mkdir("prod_list")

    # 파일 만들어서 저장하기
    def file_write(self):
        import Zentrade.zen.Product_list as wholepage
        self.no =wholepage.Whole_list().parser_wholelist()
        for num in self.no:
            No = num[:][0]

            url = self.prodctlist+str(No)+"&category="
            login_res = session.get(url,headers=self.prodctlist_url_header).text
            self.make_directory()
            html_file = open(f'./prod_list/' + self.name_mall + '_' + self.name_code_mall + '_' + self.code_mall + '_' +
                             str(No) + '.html', 'w', encoding='cp949')

            html_file.write(login_res)

            html_file.close()

        return str(No)



    def prod_list(self):
        prod_detail_list = []
        mall = DataZenProductList()
        path ='d:/data/prod_list/'
        file_list = os.listdir(path)
        filename = [file for file in file_list if file.endswith('.html') ]
        for file in filename:
            self.html_file = open(f'd:/data/prod_list/'
                                  +file,  'r', encoding='cp949')
            html = BS(self.html_file, "html.parser")
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
                prod_price = prod_price[0].string.replace(",",'')

                # 배송비
                deli_price = prod_deli[0].string.replace(",", '')

                # 카테고리
                category = category[0].string
                # 제목
                self.prod_name = prod_name[0].string
                # 상품번호
                prod_num = prod_num[1].string.replace("상품번호 : ", "")
                # print(prod_num)
                # 변동내용(변경항목,상세내용,변경일시)
                changedlist = changelist[0].string
                detail_text = changelist[1].string
                change_date = changelist[2].string


                mall.timestamp =cu.getDateToday()
                mall.code_mall = self.code_mall
                mall.name_mall = self.name_mall
                mall.name_code_mall =self.name_code_mall
                mall.category = category
                mall.prod_num = prod_num
                mall.prod_name = self.prod_name
                mall.prod_price =prod_price
                mall.prod_date = ''
                mall.country = country
                mall.prod_tax = prod_tax
                mall.deli_price = deli_price
                mall.deli_detail1 = deli_detail1
                mall.deli_detail2 = deli_detail2
                mall.changedlist = changedlist
                mall.detail_tax = detail_text
                mall.change_dete = change_date

                mall.set_date_dict()
                tmp_dict = mall.get_date_dict()
                newlist = [i for i in tmp_dict.values()]

                prod_detail_list.append(tmp_dict)

        return prod_detail_list



#
# a=Product_List()
# # a.mall_login()
# # a.file_write()
# a.prod_list()

if __name__ == '__main__':
    # insert
    # test = 'insert'
    # 검색
    test = 'search'
    # test = 'search_all'
   #  create file
   #  test = 'createfile'
   # login
   #  test = 'login'
    detail= Product_List()
    # -------------------------#
    # 코드명
    code_mall = detail.code_mall
    # 상품명
    name = '휴지'
    indexname = 'product_detail'


    # insert
    if test == 'insert':

        mall = DataZenProductList()
        DataMallProddetail().insertbulk_prod_detail(Product_List().prod_list(),indexname)

    # code_mall 하나로 검색하는방법
    if test == 'search':
        malles = DataMallProddetail()

        mall_code_res = malles.search_mall_code(code_mall,indexname)
        print('mall_code : ', mall_code_res)
        all_data = malles.result_all_productdetail(mall_code_res)
        for it in all_data:
            print(it.get_date_dict())
        print('len : ', len(all_data))

    # 전체 검색
    if test == 'search_all':
        malles = DataMallProddetail()
        malles_search_all = malles.getAllProddetail(indexname)
        print('mall_code : ', malles_search_all)
        all_data = malles.result_all_productdetail(malles_search_all)
        for it in all_data:
            print(it.get_date_dict())
        print('len : ', len(all_data))
