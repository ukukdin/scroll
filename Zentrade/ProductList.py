import re

import pandas as pd
import requests
from bs4 import BeautifulSoup as BS

import datetime

session = requests.Session()
loginPage = "https://www.zentrade.co.kr/shop/member/login_ok.php"
LOGIN_INFO = {
    "return_url" : "https://www.zentrade.co.kr/shop/goods/goods_list.php?&page=",
    "m_id": "hitrend",
    "password": "!qaz2wsx3edc"

}
login_res = session.post(loginPage, data=LOGIN_INFO)

file = 'd:/list3.csv'
r =pd.read_csv(file,encoding='cp949')
w= r['Num'].values

result=[]
def list(result):
    for pli in w:
        prodctlist = "https://www.zentrade.co.kr/shop/goods/goods_view.php?goodsno="+str(pli)+"&category="
        login_res = session.get(prodctlist)
        login_res.raise_for_status()
        html = BS(login_res.text, "html.parser")
        login_res = session.get(prodctlist)
        login_res.raise_for_status()
        html = BS(login_res.text, "html.parser")
        itemlist = html.select("div[class=indiv]")

        for detail in itemlist:
            # 카테고리
            category = detail.select("div[align=right] a")
            # 제목/상품번호
            title = detail.select("td font[style^=font-size] b")

            deli_detail = detail.select('form[name=frmView] table:nth-of-type(2) font')
            # 가격
            price = detail.select('span[id=price]')
            # 배송비
            deli = detail.select('tr[height="20"] b')
            # 배송디테일
            box = detail.select('tr[height="30"] td')
            #변동내역
            changelist = detail.select('table[align=center] tr:nth-of-type(2) td')

            # 색상정보
            option = detail.select('select[name^=opt]')
            for o in option:
                option_detail = o.get_text(strip=True).replace("== 옵션선택 ==","")

              # 원산지
            country = box[0].string
            # 과세여부
            tax = box[1].string
            # 배송디테일
            deli1 = deli_detail[0].string
            deli2 = deli_detail[1].string
            # 가격
            price = price[0].string
            # 배송비
            deli_price = deli[0].string
            # 카테고리
            category = category[0].string
            # 제목
            Title = title[0].string
            # 상품번호
            Num = title[1].string
            # 변동내용(변경항목,상세내용,변경일시)
            changedlist = changelist[0].string
            detail_text = changelist[1].string
            change_data = changelist[2].string


            result.append([category]+[Title]+[Num]+
                          [price]+[country]+[tax]+
                          [deli_price]+[deli1]+[deli2]
                          +[option_detail]+[changedlist]+[detail_text]
                          +[change_data])



def main():
    result=[]
    print("ZenTrade의 전체상품 리스트")
    list(result)
    list_table = pd.DataFrame(result,columns=('Category','title','Num',
                                              'price','country','tax',
                                              '배송비','도서,산간,지역','선불/착불',
                                              '옵션',
                                              '변경항목','상세내용','변경일시'))
    list_table.to_csv('d:/zentrade/list1.csv',encoding='cp949',mode='w',index=True)
    del result[:]
if __name__=='__main__':
    main()

