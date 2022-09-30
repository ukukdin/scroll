from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
category = {
    "cpu" : "873",
    "메인보드":"875",
    "메모리": "874",
    "그래픽카드" : "876",
    "ssd" : "32617",
    "케이스":"879",
    "파워":"880",

}

category_css={
    c:"dd.category_" + category[c]+ " a" for c in category
 }

options = webdriver.ChromeOptions()
options.add_argument("window-size=1120,1020")
options.add_argument("no-sandbox")

chrome = webdriver.Chrome("D:/chromedriver")
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)


def find(wait,css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,css_selector)))


def find_present(css):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,css)))

def finds_present(css):
    find_present(css)
    return chrome.find_elements(By.CSS_SELECTOR,css)
def find_visible(css):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

def finds_visible(css):
    find_visible(css)
    return chrome.find_elements(By.CSS_SELECTOR,css)
def rightFrame():
    find_visible("iframe#ifrmWish")
    chrome.switch_to.frame("ifrmWish")
def leftFrame():
    find_visible("iframe#ifrmProduct")
    chrome.switch_to.frame("ifrmWish")

def choose_one(text,options):
    print("--------")
    print(text)
    print("--------")
    for i in range(len(options)):
        print(f"{i+1}.{options[i]}")
    choose = input("-> ")
    return int(choose)-1

def go_to_category(category_name):
    find_visible(category_css[category_name]).click()
    time.sleep(1)



def parse_products():
    products=[]
    for p in finds_visible("div.scroll_box tr[class^=productList_]"):
        title = p.find_element(By.CSS_SELECTOR, "p.subject a").text
        try:
            price = p.find_element(By.CSS_SELECTOR, "span.prod_price").text
        except:
            continue
        products.append((title, price))
    return products

def choose_maker(num,text):

    options = finds_visible("div[class^=search_option_list] div:nth-of-type("+num+") div[class^=search_cate_contents]  span[class=item_text]")
    i = choose_one(text + "를 골라주세요", [x.text for x in options])
    options[i].click()
    time.sleep(1)
    return i

def see_more(num):
    return find_visible("div[class=search_option_list] div:nth-of-type("+ num +") button[class=btn_item_more]").click()

def get_option(num):
  options = finds_visible("div[class^=search_option_list] div:nth-of-type(" + num + ") div[class^=search_cate_contents]  span[class=item_text]")
  if is_intel:
      options[0].click()
  elif is_amd:
      options[1].click()
chrome.get("https://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_gnb_esti")
# chrome.find_elements(By.CSS_SELECTOR,"div[class=main-header__nav] a[class=link_nav]")[2].click()
# chrome.switch_to.window(chrome.window_handles[1])
# cpu 가져오기
go_to_category("cpu")

time.sleep(1)
# cpu 제조사 불러오기

make_idx = choose_maker("1","cpu")



is_intel=False
is_amd=False
title=""
if make_idx ==0:
    is_intel=True
    find_visible("div[class=search_option_list] div:nth-of-type(2) button[class=btn_item_more]").click()
    title = "div[class=search_option_list] div:nth-of-type(2) div[class^=search_cate_contents] li[class^=search_cate_item]"
elif make_idx ==1:
    is_amd=True
    find_visible("div[class=search_option_list] div:nth-of-type(3) button[class=btn_item_more]").click()
    title = "div[class=search_option_list] div:nth-of-type(3) div[class^=search_cate_contents] li[class^=search_cate_item]"

options = finds_visible(f"{title}")
i =choose_one("CPU 종류 를 골라주세요",[x.text for x in options])
options[i].click()
time.sleep(1)

'''# cpu 목록 선택하기
상품명 가져오기 
tr[class^=productList_] p[class=subject]
가격 
tr[class^=productList_] span[class=prod_price]
'''
'''options = finds_visivle(tr[class^=productList_] p[class=subject])
i choose_one("",[x.text for x in options])
options[i].click()'''

# cpu 목록 가져오기
cpus =parse_products()
# for cpu in cpus:
#     print(cpu)
# time.sleep(10)


'''-----------------------------------main board ------------------------------------------------------'''
# 메인보드 가져오기

go_to_category("메인보드")
see_more("1")
# # 메인보드 고르는 방법
choose_maker("1","메인보드")
get_option("2")
time.sleep(1)
mainboards = parse_products()
for mb in mainboards:
    print(mb)


"------------------------메모리=---------------------"
go_to_category("메모리")
see_more("1")
choose_maker("1","메모리")
'''제품 분류 선택'''
get_option("2")

"---------------------------그래픽카드--------------------"
go_to_category("그래픽카드")
see_more("1")
choose_maker("1","그래픽카드")
# 칩셋 제조사
get_option("2")
