from bs4 import BeautifulSoup as BS
import requests
from Zentrade.zen_product_out.data_product_out import DataProductOut
from Zentrade.index_zentrade.zen_lib_detail import DataMallProddetail
import os
import Crawling.common.util_common as cu

# 품절페이지
class out_of_stock():
    def __init__(self):
        super(out_of_stock, self).__init__()

        self.session = requests.Session()
        self.loginPage = "https://www.zentrade.co.kr/shop/member/login_ok.php"
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
        self.prod_out_url1 = 'https://www.zentrade.co.kr/shop/goods/goods_soldout.php?category=&sort=b.updatedt+desc%2C+b.goodsno+desc&page_num=80&resale_yn=all'
        self.prod_out_url = 'https://www.zentrade.co.kr/shop/goods/goods_view.php?goodsno='
        self.prod_out_url_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Length": "77",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "zent_login_id=hitrend; gd_user_enamooPass=XXdndUlRb2NNUmVyRVBJck09My5JUyx0SmdZK01oPzJGQF93SWRyOw%3D%3D; PHPSESSID=f786be587b670e875bac496f49b696d9; godoLog=20221013; shop_authenticate=Y; cookie_check=0;",
            "Host": "zentrade.co.kr",
            "Origin": "http://zentrade.co.kr",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        }
        self.info = {
            "m_id": "hitrend",
            "password": "!qaz2wsx3edc"
        }
        self.code_mall = 'M0000003'
        self.name_mall = 'zentrade'
        self.name_code_mall = 'Out_of_product'



    def mall_login(self):
        login_res = self.session.post(self.loginPage, self.info, self.login_header)
        print(login_res.text)

    def make_directory(self):
        os.chdir("D:/data/")
        if os.path.isdir("D:/data/outofstock"):
            pass
        else:
            os.mkdir("outofstock")
    def file_write(self):
        url = self.prod_out_url1
        login_res = self.session.get(url).text
        self.make_directory()
        html_file = open(
            f'./outofstock/' + self.name_mall + '_' + self.name_code_mall + '_' + self.code_mall +
                '.html', 'w', encoding='cp949')
        html_file.write(login_res)
        html_file.close()
        print('완료')




    def outstock(self):
        stock = []
        mall = DataProductOut()
        html = self.file_open()
        ranged = html.findAll("font", attrs={"color": "#000000"})
        detail = html.select("td table[class=outline_both]")
        for i in ranged:
            num = i.findAll("b")
            range_num = num[0].string
            for page in range(int(range_num)):
                for so in detail:
                    # 상품번호
                    producted_num = so.select("td:nth-of-type(1) font[style^=font] b")
                    prod_num = producted_num[page].string

                    # 상품정보
                    producted_detail = so.select("font a")
                    prod_name = producted_detail[page].string
                    # # 가격
                    priced = so.select("b[class=blue]")
                    prod_price = priced[page].string.replace(',', '')

                    # # 재고정보
                    out = so.select("span[style^=background] font")
                    prod_out = out[page].string

                    # # 재입고여부
                    reordered = so.find_all("td", {"height": "50"})
                    reorder = reordered[page].string

                    #  제품 품절이유
                    reasoned = so.select("td[align=left] font")
                    reason = reasoned[page].text.replace("\n", "")

                    # 재입고예정일
                    # 재입고 예정일 1번째단
                    delete_dated1 = so.select("tr:nth-child(1) td:nth-of-type(3)")
                    b = []
                    b.append(delete_dated1[1])
                    reorder_dated = so.select("td:nth-of-type(6)")
                    reorder_da = b + reorder_dated
                    # 재입고예정일 최종
                    reorder_date = reorder_da[page].text

                    # 삭제예정일 첫번째단
                    delete_dated2 = so.select("tr:nth-child(1) td:nth-of-type(4)")
                    delete_dated = so.select("td:nth-of-type(7)")
                    a = []
                    a.append(delete_dated2[1])
                    expire_dated = a + delete_dated
                    # 삭제예정일 첫번째단 최종
                    expire_date = expire_dated[page].text

                    tmp_dict = self.mall_list(expire_date, mall, prod_name, prod_num, prod_out, prod_price, reason,
                                              reorder, reorder_date)
                    stock.append(tmp_dict)


        return stock

    def mall_list(self, expire_date, mall, prod_name, prod_num, prod_out, prod_price, reason, reorder, reorder_date):
        mall.timestamp = cu.getDateToday()
        mall.code_mall = self.code_mall
        mall.name_mall = self.name_mall
        mall.name_code_mall = self.name_code_mall
        mall.prod_out_url = self.prod_out_url+str(prod_num)+'category='
        mall.prod_num = prod_num
        mall.prod_name = prod_name
        mall.prod_price = prod_price
        mall.prod_out = prod_out
        mall.reason = reason
        mall.reorder = reorder
        mall.reorder_date = reorder_date
        mall.expire_date = expire_date
        mall.set_date_dict()
        tmp_dict = mall.get_date_dict()
        return tmp_dict

    def file_open(self):
        html_file = open(
            f'd:/data/outofstock/' + self.name_mall + '_' + self.name_code_mall + '_' + self.code_mall + '.html', 'r',
            encoding='cp949')
        html = BS(html_file, "html.parser")
        return html


#
# if __name__ =='__main__':
#     test = 'insert'
#     # test = 'createfile'
#     # test = 'login'
# #     test = 'update'
#     # test = 'searchall'
#     # ot = out_of_stock()
# #     if test == 'createfile':
# #         ot.file_write()
#     prod_name = '품절상품입니다.'
#     indexname ='product_list'
#     index_name = 'product_list'
#
#     if test =='login':
#         ot.mall_login()
#     if test == 'createfile':
#         ot.file_write()
# #
# #
#     if test =='insert':
#         mall = DataMallProddetail()
#         DataMallProddetail().insertbulk_prod(out_of_stock().outstock(),indexname)

    # for i in ot.outstock():
    #     no = list(i.values())[5]
    #     print(no)
    #     if test == 'update':
    #         mall = DataMallProddetail()
    #         mall_prodnum = mall.search_mall_code(no,index_name)
    #         # update 위한 id 구하는 구문
    #         a= list(mall_prodnum.values())[3]
    #         b=list(a.values())[2]
    #         for a in b:
    #             # 최종 update doc id
    #             ids = list(a.values())[2]
    #             all_data = mall.result_all_data_product(mall_prodnum)
    #             # for it in all_data:
    #                 # print(it.get_date_dict())
    #             if no != None:
    #                 mall.update_mall_code(prod_name, index_name,ids)
    #                 print('업데이트중 판매 종료 알림')
    #             else:
    #                 print('중복이 없습니다. ')
    #
    #


