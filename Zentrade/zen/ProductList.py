from bs4 import BeautifulSoup as BS
import requests
import os




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
            "Cookie": "zent_login_id=hitrend; PHPSESSID=12efce5a2457f686a5ac4fc32496e07d; shop_authenticate=Y; cookie_check=0; zent_main_search_skey=b.goodsno; gd_user_enamooPass=XXdndUlRb2NNUmVyRVBJck09My5JUyx0SmdZK01oRy5FdlUxSWRyOw%3D%3D; Xtime=1665635370;",
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
            'Cookie': 'PHPSESSID=12efce5a2457f686a5ac4fc32496e07d; shop_authenticate=Y; zent_login_id=hitrend; cookie_check=0',
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
        self.login_res = session.post(self.login_url, self.info,self.login_header)

    def make_directory(self):
        os.chdir("D:/data/")
        if os.path.isdir("D:/data/prod_list"):
            pass
        else:
            os.mkdir("prod_list")

    # 파일 만들어서 저장하기
    def file_write(self):
        import Zentrade.zen.p as wholepage
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
        path ='d:/data/prod_list/'
        file_list = os.listdir(path)
        filename = [file for file in file_list if file.endswith('.html') ]
        for file in filename:

            self.html_file = open(f'd:/data/prod_list/' + file, 'r', encoding='cp949')

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

                    # 변동내역
                    changelist = detail.select('table[align=center] tr:nth-of-type(2) td')

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
                    prod_tax = country_tax[1].string.replace('\n','')
                    # # 배송디테일
                    deli_detail1 = deli_detail[0].string
                    deli_detail2 = deli_detail[1].string

                    # # 가격
                    prod_price = prod_price[0].string.replace(',','')
                    # 배송비
                    # deli_price = prod_deli[0].string.replace(",",'')
                    # print(deli_price)
                    # 카테고리
                    category = category[0].string
                    # 제목
                    prod_name = prod_name[0].string
                    # 상품번호
                    prod_num = prod_num[1].string.replace("상품번호 : ","" )
                    # print(prod_num)
                    # 변동내용(변경항목,상세내용,변경일시)
                    changedlist = changelist[0].string
                    detail_text = changelist[1].string
                    change_date = changelist[2].string

                    prod_detail_list.append([prod_num] + [prod_name] + [category] + [prod_price]+[country]+[prod_tax]+[deli_detail1]+[deli_detail2]+
                                             [changedlist]+[detail_text]+[change_date])

        print(prod_detail_list)
        return prod_detail_list
# #
a= Product_List()
# a.__init__()
# a.file_write()
a.prod_list()