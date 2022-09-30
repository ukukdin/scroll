import re

import pandas as pd
import requests
from bs4 import BeautifulSoup as BS
import requests as req
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
#
# options = webdriver.ChromeOptions()
# options.add_argument("no-sandbox")
# options.add_argument("--headless")==True
# chrome = webdriver.Chrome("D:/chromedriver", options=options)
# wait = WebDriverWait(chrome, 10)
# url = chrome.get("https://www.zentrade.co.kr/shop/goods/goods_list.php?&page=")
#
# def find(wait, css_select):
#     return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_select)))
# def find_visible(css):
#     return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
#
# def finds_visible(css):
#     find_visible(css)
#     return chrome.find_elements(By.CSS_SELECTOR,css)
#
# input_id = find(wait, "input[name=m_id]")
# input_pw = find(wait, "input[name=password]")
#
# pyperclip.copy("hitrend")
#
# input_id.send_keys(Keys.CONTROL,"v") #윈도우에서 사용하는 방식(컨트롤v 즉 복사해서 넣겠다.)
# pyperclip.copy("!qaz2wsx3edc")
# input_pw.send_keys(Keys.CONTROL,"v")
# find_visible("form[name=mainloginform] input:nth-of-type(3)").click()

session = requests.Session()
loginPage = "https://www.zentrade.co.kr/shop/member/login_ok.php"
LOGIN_INFO = {
    "return_url" : "https://www.zentrade.co.kr/shop/goods/goods_list.php?&page=",
    "m_id": "hitrend",
    "password": "!qaz2wsx3edc"

}
login_res = session.post(loginPage, data=LOGIN_INFO)
#
result=[]
# def list(result):
#     for page in range(1,2):
#          url ="https://www.zentrade.co.kr/shop/goods/goods_list.php?&page="+str(page)
#          login_res = session.get(url)
#          login_res.raise_for_status()
#          html = BS(login_res.text, "html.parser")
#          tag_table = html.select('td[width="25%"]')
#          # print(tag_table)
#          for productList in tag_table:
#               tt = productList.select('div')
#               num = tt[2].string
#               name = tt[3].string
#               ttt = productList.select('b')
#               price = ttt[0].string
#               result.append([num]+[name]+[price])
#     return
prodctlist = "https://www.zentrade.co.kr/shop/goods/goods_view.php?goodsno=4263&category="
login_res = session.get(prodctlist)
login_res.raise_for_status()
html = BS(login_res.text, "html.parser")


itemlist = html.select("form[name=frmView]")
for detail in itemlist:

    deli_detail = detail.select('table:nth-of-type(2) font')

    price =detail.select('span[id=price]')

    deli = detail.select('tr[height="20"] b')

    box = detail.select('tr[height="30"] td')
    option = detail.select('select option[value^="가-힣"]')

    # print(deli[0].string+"원")
    # 원산지
    country = box[0].string
    # 과세여부
    tax = box[1].string
    # 배송디테일
    deli_detail[0].string
    deli_detail[1].string

    print(country,tax,option)
#
# price = html.select('span[class=sprice]')
# # 원산지


# chrome.quit()

# def main():
#     result=[]
#     print("ZenTrade의 전체상품 리스트")
#     list(result)
#     list_table = pd.DataFrame(result,columns=('Num','Name','Price'))
#     list_table.to_csv('d:/list.csv',encoding='cp949',mode='w',index=True)
#     del result[:]
# if __name__=='__main__':
#     main()

