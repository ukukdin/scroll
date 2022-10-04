import re
import pandas as pd
from bs4 import BeautifulSoup as BS
import requests
import datetime

session = requests.Session()
loginPage = "https://www.zentrade.co.kr/shop/member/login_ok.php"
LOGIN_INFO = {
    "return_url" : "https://www.zentrade.co.kr/shop/goods/goods_list.php?&page=",
    "m_id": "hitrend",
    "password": "!qaz2wsx3edc"

}
login_res = session.post(loginPage, data=LOGIN_INFO)
Sold_out = "https://www.zentrade.co.kr/shop/goods/goods_soldout.php?&page="
login_res = session.get(Sold_out)
login_res.raise_for_status()
html = BS(login_res.text, "html.parser")
detail = html.select("td table[class=outline_both]")

result=[]
# def list(result):
for page in range(1):
    for so in detail:
        # 상품번호
        producted_num = so.select("td:nth-of-type(1) font[style^=font] b")


        prd_num = producted_num[page].string
        # print(prd_num)
        # # 상품정보
        # producted_detail = so.select("font a")
        # prod_detail = producted_detail[page].string
        # print(prod_detail)
        # # # 가격
        # priced = so.select("b[class=blue]")
        # price = priced[page].string
        # print(price)
        # # # 제고정보
        # outt = so.select("span[style^=background] font")
        # out = outt[page].string
        # print(out)
        # # # 재입고여부
        # #
        # reordered = so.select("td[align=center] b font")
        # reorder = reordered[page].string
        # print(reorder)
        #
        # #  제품 품절이유
        #
        # reasoned = so.select("td[align=left] font")
        # print(reasoned[page].text)

        # 재입고예정일

        reorder_date = so.select("tr td:nth-of-type(6)")
        print(reorder_date[page].text)


              # # 삭제예정일
        # delete_dated = so.select("td:nth-of-type(7)")
        # print(delete_dated[page].text)
        # # print(delete_dated[page].text)
        # for dele in delete_dated:
        #     dele.text
        # # print(dele.text)




    # result.append([prd_num]+ [prod_detail]+[price]+[out]+[reorder]+[reord_date]+[del_date]+[reason])
    #
    # return

# #'판매가','재입고여부','재입고예정일','삭제예정일','품절이유'
# def main():
#     result=[]
#     print("ZenTrade의 전체상품 리스트")
#     list(result)
#     list_table = pd.DataFrame(result,columns=('상품번호','상품정보','가격','제고정보','재입고여부','재입고예정일','삭제예정일','품절이유'))
#     list_table.to_csv('C:/Users/User/pythonProject12/list.csv', encoding='cp949',mode='w',index=True)
#     del result[:]
# if __name__=='__main__':
#     main()
#


'''
  for so in detail:
        # 상품번호
        producted_num = so.select("td:nth-of-type(1) font[style^=font] b")
        for num in producted_num:
            product_num = num.text
        # 상품정보
            producted_detail = so.select("font a")
            for pd in producted_detail:
                product_detail = pd.text

                        # 제고정보
                outt = so.select("span[style^=background] font")
                for outstock in outt:
                    out = outstock.text

                    # 가격
                    priced = so.select("b[class=blue]")
                    for pr in priced:
                        price = pr.text

        # 재입고여부
                    reordered = so.select("td[align=center] b font")
                    for re in reordered:
                        reorder = re.text
                        # 재입고예정일
                        reorder_date = so.select("td:nth-of-type(6) font")
                        for reorder_dated in reorder_date:
                            date = reorder_dated.text.replace("입", ' 입')
                            # 제품 품절이유
                            reasoned = so.select("td[align=left] font")
                            for res in reasoned:
                                reason = res.text
                                # 삭제예정일
                                delete_dated = so.select("td:nth-of-type(7)")
                                for delete_datee in delete_dated:
                                    delete_date = delete_datee.text

'''