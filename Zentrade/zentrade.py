import time
from bs4 import BeautifulSoup

from Crawling.common.lib_request import RequestHit
import Crawling.common.util_fileloader as fl
import Crawling.common.util_common as cu
from Crawling.mall.lib.data_prodlist import DataMallProdlist
from Crawling.mall.lib.es_pordlist import DataMallProdlistES
import random

class zentrade(RequestHit):
    def __init__(self):
        super(zentrade, self).__init__()

        info = {
            "m_id": "hitrend",
            "password": "!qaz2wsx3edc"
        }
        self.gubun = 'mall'
        self.path = 'product'
        self.exp_html = '.html'
        self.fpath_prodlist = None
        self.flist_prodlist = None

        # Data - file
        self.date = None

        self.mall_category = {
            '001':'문구/사무용품',
            '004':'생활용품',
            '005':'주방/욕실용품',
            '007':'디지털/자동차',
            '009':'여행/캠핑/취미',
            '011':'패션/이미용/건강',
            '012':'유아동/출산',
        }
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
            "Host": "chaesiknara.co.kr",
            "Origin": "http://chaesiknara.co.kr",
            "Referer": "http://chaesiknara.co.kr/shop/member/login.php?&",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        }
        # 전체상품

        self.Whole_prod_url = "https://www.zentrade.co.kr/shop/goods/goods_list.php?&page="
        self.Whole_prod_url_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Length": "77",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "PHPSESSID=e9o0rmmdnf76i0ehe7597cf126; cookie_check=0; godoLog=20210916; shop_authenticate=Y; _fbp=fb.2.1631754439491.1397331112; Xtime=1631754469; wcs_bt=s_29f5659006d8:1631754472",
            "Host": "chaesiknara.co.kr",
            "Origin": "http://chaesiknara.co.kr",
            "Referer": "http://chaesiknara.co.kr/shop/member/login.php?&",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        }
        # 품절상품
        self.Sold_out_url = 'https://www.zentrade.co.kr/shop/goods/goods_soldout.php?category=&sort=b.updatedt+desc%2C+b.goodsno+desc&page_num=40&resale_yn=all'
        self.Sold_out_url_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Length": "77",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "PHPSESSID=e9o0rmmdnf76i0ehe7597cf126; cookie_check=0; godoLog=20210916; shop_authenticate=Y; _fbp=fb.2.1631754439491.1397331112; Xtime=1631754469; wcs_bt=s_29f5659006d8:1631754472",
            "Host": "chaesiknara.co.kr",
            "Origin": "http://chaesiknara.co.kr",
            "Referer": "http://chaesiknara.co.kr/shop/member/login.php?&",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        }
        # 신상품
        self.new_prod_url = "https://www.zentrade.co.kr/shop/goods/goods_new.php?searchDate=" + cu.getDateToday()
        self.new_prod_url_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Length": "77",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "PHPSESSID=e9o0rmmdnf76i0ehe7597cf126; cookie_check=0; godoLog=20210916; shop_authenticate=Y; _fbp=fb.2.1631754439491.1397331112; Xtime=1631754469; wcs_bt=s_29f5659006d8:1631754472",
            "Host": "chaesiknara.co.kr",
            "Origin": "http://chaesiknara.co.kr",
            "Referer": "http://chaesiknara.co.kr/shop/member/login.php?&",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        }

        def close_sess_es(self):
            self.sess.close()
            self.malles.closeConnectES()
            # 파일에 들어갈 날짜

        def setDate(self, date):
            self.date = date

        def mall_login(self):
            resp = self.request_post(self.login_url, self.login_header, self.info)
            print(resp.text)