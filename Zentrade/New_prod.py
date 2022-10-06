import re
import pandas as pd
import requests
from bs4 import BeautifulSoup as BS
import requests as req
import datetime as date
import Crawling.common.util_common as cu

session = requests.Session()
loginPage = "https://www.zentrade.co.kr/shop/member/login_ok.php"
LOGIN_INFO = {
    "m_id": "hitrend",
    "password": "!qaz2wsx3edc"
}

print(cu.getDateToday())
login_res = session.post(loginPage, data=LOGIN_INFO)
new_prod_url ="https://www.zentrade.co.kr/shop/goods/goods_new.php?searchDate="+cu.getDateToday()
login_res = session.get(new_prod_url)
login_res.raise_for_status()
html = BS(login_res.text, "html.parser")
new_list = html.findAll("td", attrs={"bgcolor":"FFD9EC","height":"40","id":"b_white","style":"padding-left:15px;"})

for i in new_list:
     num=i.findAll("b")
     prod_num = num[1].string
     if prod_num == str(0):
        print("오늘의 신상품은 없습니다.")
     else:
         print("오늘의 신상품은 "+ str(prod_num)+"개의 상품이 있습니다.")
         print()
         prod_list = html.findAll("td",attrs={'align':'center','valign':'top','width':'25%'})
         for list in prod_list:
             detail = list.select('div')
             # 신상품 등록일
             new_prod_date = detail[2].string.replace("신상품 등록일 : ","")
             # 새로운 상품 번호
             new_prod_num = detail[3].string.replace("No. ", "")
             # 새로운 상품 이름
             new_prod_name = detail[4].string
             p = detail[1].select('b')
             new_prod_price = p[0].string

             print("가격은:",new_prod_price,'\n'
                   "제품명",new_prod_name,'\n'
                   "제품번호",new_prod_num,'\n'
                   "신상품 등록일",new_prod_date,'\n')
