import re
import pandas as pd
from bs4 import BeautifulSoup as BS
import requests
import datetime

session = requests.Session()
loginPage = "https://www.zentrade.co.kr/shop/member/login_ok.php"
LOGIN_INFO = {
    "m_id": "hitrend",
    "password": "!qaz2wsx3edc"
}
login_res = session.post(loginPage, data=LOGIN_INFO)

Sold_out_url = 'https://www.zentrade.co.kr/shop/goods/goods_soldout.php?category=&sort=b.updatedt+desc%2C+b.goodsno+desc&page_num=40&resale_yn=all'
login_res = session.get(Sold_out_url)
html = BS(login_res.text, "html.parser")
detail = html.select("td table[class=outline_both]")
ranged = html.findAll("font", attrs={"color":"#000000"})
def range_num():
    for i in ranged:
        num=i.findAll("b")
        range_num =num[0].string
    return range_num
for page in range(int(range_num())):
    for so in detail:
        # 상품번호
            producted_num = so.select("td:nth-of-type(1) font[style^=font] b")
            prod_num = producted_num[page].string
            # 상품정보
            producted_detail = so.select("font a")
            prod_name = producted_detail[page].string
            # # 가격
            priced = so.select("b[class=blue]")
            prod_price = priced[page].string

            # # 제고정보
            outt = so.select("span[style^=background] font")
            prod_out = outt[page].string

            # # 재입고여부
            reordered = so.find_all("td", {"height": "50"})
            reorder = reordered[page].string

            #  제품 품절이유
            reasoned = so.select("td[align=left] font")
            reason = reasoned[page].text

            # 재입고예정일
            # 재입고 예정일 1번째단
            delete_dated1 = so.select("tr:nth-child(1) td:nth-of-type(3)")
            b = []
            b.append(delete_dated1[1])
            reorder_dated = so.select("td:nth-of-type(6)")
            reorder_da = b + reorder_dated
            reorder_date = reorder_da[page].text

            # 삭제예정일 첫번째단
            delete_dated2 = so.select("tr:nth-child(1) td:nth-of-type(4)")
            delete_dated = so.select("td:nth-of-type(7)")
            a = []
            a.append(delete_dated2[1])
            expire_dated = a + delete_dated
            expire_date = expire_dated[page].text

