from bs4 import BeautifulSoup as BS
import requests
import os
from Zentrade.zen_product.Product_list import Whole_list
from Zentrade.zen_new_product.data_new_Product_detail import DataZenProductList
from Zentrade.index_zentrade.zen_lib_detail import DataMallProddetail
import Crawling.common.util_common as cu
import New_product_list as Np
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
        self.new_prod = Np.New_List().NP()
        for a in self.new_prod:
            self.No = list(a.values())[5]
            # print(self.No)
            url = self.prodctlist + str(self.No) + "&category="
            # print(url)
            login_res = session.get(url).text
            self.make_directory()
            html_file = open(
                f'./new_prod_list/' + self.name_mall + '_' + self.name_code_mall + '_' + self.code_mall + '_' +
                str(self.No) + '.html', 'w', encoding='cp949')
            html_file.write(login_res)
            html_file.close()

        return str(self.No)





    def new_prod_list(self):
        new_prod_detail_list = []
        mall = DataZenProductList()
        path  = 'd:/data/new_prod_list/'
        file_list = os.listdir(path)
        filename = [file for file in file_list if file.endswith('.html') ]
        for filed in filename:

            self.html_file = open(f'd:/data/new_prod_list/'
                                  + filed, 'r', encoding='cp949')
            html = BS(self.html_file, "html.parser")
            itemlist = html.select("div[class=indiv]")
            for detail in itemlist:
                # 카테고리
                category = detail.select("div[align=right] a")
                # 제목/상품번호
                prod_name = detail.select("td font[style^=font-size] b")
                prod_num = detail.select("td[align=center] font b")

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
                # option = detail.select('select[name^=opt]')
                # for o in option:
                #     option_detail = o.get_text(strip=True).replace("== 옵션선택 ==", "")
                # 원산지
                country = country_tax[0].string
                # 과세여부
                prod_tax = country_tax[1].string.replace('\n','')
                # # 배송디테일
                deli_detail1 = deli_detail[0].string
                deli_detail2 = deli_detail[1].string

                # # 가격
                prod_price = prod_price[0].string.replace(",",'')
                # 배송비
                deli_price = prod_deli[0].string.replace(',','')
                # 카테고리
                category = category[0].string
                # 제목
                prod_name = prod_name[0].string
                # 상품번호
                prod_num = prod_num[1].string.replace('상품번호 : ','')
                print(prod_num)
                # 변동내용(변경항목,상세내용,변경일시)

                changedlist = changelist[0].string
                detail_text = changelist[1].string
                change_date = changelist[2].string


                mall.timestamp = cu.getDateToday()
                mall.code_mall = self.code_mall
                mall.name_mall = self.name_mall
                mall.name_code_mall = self.name_code_mall
                mall.category = category
                mall.prod_num = prod_num
                mall.prod_name = prod_name
                mall.prod_price = prod_price
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
                # print(tmp_dict)
                newlist = [i for i in tmp_dict.values()]
                new_prod_detail_list.append(tmp_dict)

        return new_prod_detail_list

#
# a= Product_List()
# # # a.__init__()
# # a.file_write()
# a.new_prod_list()
if __name__ =='__main__':
    indexname = 'new_prod_detail'
    index_name = 'product_detail'

    # test = 'insert'
    test ='update'
    test='search'

    # 상품번호로 검색
    prod_num = '4204'




    # 상세상품 insert
    if test == 'insert':
        mall = DataMallProddetail()
        mall.insertbulk_prod(Product_List().new_prod_list(),indexname)

    # 상세상품 update
    npd = Product_List()
    for i in npd.new_prod_list():
        print(i)
        no = list(i.values())[5]
        if test == 'update':
            mall = DataMallProddetail()
            mall_prodnum = mall.search_mall_code(no, index_name)

            # update 위한 id 구하는 구문
            a = list(mall_prodnum.values())[3]
            b = list(a.values())[2]
            for a in b:
                # 최종 update doc id
                ids = list(a.values())[2]
                if no == None:
                    mall.update_mall_coded(Product_List().new_prod_list(), index_name, ids)
                    print('신상품 등록합니다. ')
                else:
                    print('이미 등록된 상품입니다. ')
    # 상세 상품 검색
    if test == 'search':
        malles = DataMallProddetail()

        mall_code_res = malles.search_mall_code(prod_num, indexname)
        print('mall_code : ', mall_code_res)
        all_data = malles.result_all_data_newproduct(mall_code_res)
        for it in all_data:
            print(it.get_date_dict())
        print('len : ', len(all_data))
