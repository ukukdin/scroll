import time
from bs4 import BeautifulSoup as BS
import requests
from Crawling.common.lib_request import RequestHit
from Zentrade.index_zentrade import zen_lib_es
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
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 106.0.0.0 Safari / 537.36'
        }



        self.gubun = 'zentrade'
        self.path = 'wholepage'
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
            "return_url": "https://www.zentrade.co.kr/shop/goods/goods_list.php?&page=",
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
    # login

        self.login_res = session.post(self.login_url,self.info)

    # 폴더 생성
    def make_directory(self):
        os.chdir("D:/data/")
        if os.path.isdir("D:/data/"+self.gubun+'/'+self.path):
            pass
        else:
            os.mkdir('./'+self.gubun+'/'+self.path)
            
    # 파일 만들어서 저장
    def file_write(self):
        for page in range(52):
            page = page+1
            url = self.Whole_prod_url+str(page)
            login_res = session.get(url).text
            self.make_directory()
            html_file = open(f'./'+self.gubun+'/'+self.path+'/'+self.name_mall+'_'+self.name_code_mall+'_'+self.code_mall+'_'+str(page)+'.html','w', encoding='cp949')
            html_file.write(login_res)
            html_file.close()
        print("완료")

    # 페이지 상세 정보 가져오기
    def parser_wholelist(self):
        listproduct = []
    
        for page in range(52):
            page =page+1
            file = open(f'd:/data/'+self.gubun+'/'+self.path+'/'+self.name_mall+'_'+self.name_code_mall+'_'+self.code_mall+'_'+str(page)+'.html','r', encoding='cp949')
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

                # 상품가격
                prod_price = ttt[0].string

                listproduct.append([prod_num]+[prod_name]+[prod_price])


        return listproduct


whole=Whole_list()
 #파일 생성
# a.file_write()

# a.parser_wholelist()
if __name__ == '__main__':

    #######################
    test = 'create_file'
    test = ' login'
    test = 'insert'
    test = 'search_name'
    # test = 'parsor_one_file'

    #######################
    name = "시스맥스"

    #######################
    if test == 'create_file':
        mall.get_prodlist()
    # login
    if test == 'login':
        mall.mall_login()
    # insert
    if test == 'insert':
        filename = 'CHAES_062_20220913.html'
        mall.parsor_one_file(filename)

    if test == 'search_name':
        malles = DataMallProdlistES()
        mall_code_res = malles.search_mall_code()
        print('mall_code : ', mall_code_res)
        all_data = malles.result_all_data(mall_code_res)
        for it in all_data:
            print(it.get_data_dict())
        print('len : ', len(all_data))
    #######################
    # sess close
    mall.close_session()