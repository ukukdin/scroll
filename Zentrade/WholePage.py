import re
import pandas as pd
import requests
from bs4 import BeautifulSoup as BS
import requests as req
import datetime

session = requests.Session()
loginPage = "https://www.zentrade.co.kr/shop/member/login_ok.php"
LOGIN_INFO = {
    "return_url" : "https://www.zentrade.co.kr/shop/goods/goods_list.php?&page=",
    "m_id": "hitrend",
    "password": "!qaz2wsx3edc"

}
login_res = session.post(loginPage, data=LOGIN_INFO)



# result=[]
# def list(result):
for page in range(1,2):
         url ="https://www.zentrade.co.kr/shop/goods/goods_list.php?&page="
         login_res = session.get(url)
         login_res.raise_for_status()
         html = BS(login_res.text, "html.parser")
         tag_table = html.select('td[width="25%"]')
         # print(tag_table)
         for productList in tag_table:
              tt = productList.select('div')
              # print(tt)
              num = tt[2].string.replace("No. ","")

              name = tt[3].string
              print(name)
              ttt = productList.select('b')
              price = ttt[0].string
              # result.append([num]+[name]+[price])

    # return


# def main():
#     result=[]
#     print("ZenTrade의 전체상품 리스트")
#     list(result)
#     list_table = pd.DataFrame(result,columns=('Num','Name','Price'))
#     list_table.to_csv('d:/list3.csv',encoding='cp949',mode='w',index=True)
#     del result[:]
# if __name__=='__main__':
#     main()
#
