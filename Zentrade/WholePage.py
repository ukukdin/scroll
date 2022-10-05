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

result=[]
def list(result):
    for page in range(3):
             url ="https://www.zentrade.co.kr/shop/goods/goods_list.php?&page="+str(page)
             login_res = session.get(url)
             login_res.raise_for_status()
             html = BS(login_res.text, "html.parser")
             tag_table = html.select('td[width="25%"]')
             # print(tag_table)
             for productList in tag_table:
                  tt = productList.select('div')
                  # 숫자
                  num = tt[2].string.replace("No. ","")
                  # 상품명
                  name = tt[3].string
                  ttt = productList.select('b')
                  # 상품가격
                  price = ttt[0].string
                  result.append([num]+[name]+[price])

    return


def main():
    result=[]
    print("ZenTrade의 전체상품 리스트")
    list(result)
    list_table = pd.DataFrame(result,columns=('Num','Name','Price'))
    list_table.to_csv('d:/Whole_list.csv',encoding='cp949',mode='w',index=True)
    del result[:]
if __name__=='__main__':
    main()


Sold_out_url = 'https://www.zentrade.co.kr/shop/goods/goods_soldout.php?category=&sort=b.updatedt+desc%2C+b.goodsno+desc&page_num=40&resale_yn=all'
login_res = session.get(Sold_out_url)
html = BS(login_res.text, "html.parser")
detail = html.select("td table[class=outline_both]")
result_out_of_stock=[]
def list(result_out_of_stock):
    for page in range(24):
        for so in detail:
            # 상품번호
            producted_num = so.select("td:nth-of-type(1) font[style^=font] b")
            prd_num = producted_num[page].string
            # 상품정보
            producted_detail = so.select("font a")
            prod_detail = producted_detail[page].string
            # # 가격
            priced = so.select("b[class=blue]")

            price = priced[page].string
            # # 제고정보
            outt = so.select("span[style^=background] font")
            out = outt[page].string
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
        result_out_of_stock.append(
            [prd_num] + [prod_detail] + [price] + [out] + [reorder] + [reorder_date] + [expire_date] + [reason])

    return

#'판매가','재입고여부','재입고예정일','삭제예정일','품절이유'
def main():
    result_out_of_stock=[]
    print("ZenTrade의 전체상품 리스트")
    list(result_out_of_stock)
    list_table = pd.DataFrame(result_out_of_stock,columns=('상품번호','상품정보','가격','제고정보','재입고여부','재입고예정일','삭제예정일','품절이유'))
    list_table.to_csv('d:/zentrade/out_of_stock.csv', encoding='cp949',mode='w',index=True)
    del result_out_of_stock[:]
if __name__=='__main__':
    main()

file = 'd:/Whole_list.csv'
r =pd.read_csv(file,encoding='cp949')
w= r['Num'].values

Product_list=[]
def list(Product_list):
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


            Product_list.append([category]+[Title]+[Num]+
                          [price]+[country]+[tax]+
                          [deli_price]+[deli1]+[deli2]
                          +[option_detail]+[changedlist]+[detail_text]
                          +[change_data])

def main():
    Product_list=[]
    print("ZenTrade의 전체상품 리스트")
    list(Product_list)
    list_table = pd.DataFrame(Product_list,columns=('Category','title','Num',
                                              'price','country','tax',
                                              '배송비','도서,산간,지역','선불/착불',
                                              '옵션',
                                              '변경항목','상세내용','변경일시'))
    list_table.to_csv('d:/zentrade/prod_list.csv',encoding='cp949',mode='w',index=True)
    del Product_list[:]
if __name__=='__main__':
    main()

