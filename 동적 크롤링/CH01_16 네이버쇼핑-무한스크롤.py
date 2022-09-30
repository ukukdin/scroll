from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")  # sandbox- 크롬은 tab마다 별개의 프로세스입니다.
# options.add_argument("headless") #크롬창을 안보이게 할 떄


chrome = webdriver.Chrome("D:/chromedriver")
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get("https://shopping.naver.com/")


def find(wait, css_select):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_select)))


# login_button=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button")))

# find(wait, "a#gnb_login_button").click()
#
# input_id = find(wait, "input#id")
# input_pw = find(wait, "input#pw")
#
# pyperclip.copy("xkfcnwp")
# input_id.send_keys(Keys.CONTROL, "v")  # 윈도우에서 사용하는 방식(컨트롤v 즉 복사해서 넣겠다.)
# pyperclip.copy("dlsrnr12!")
# input_pw.send_keys(Keys.CONTROL, "v", '\n')
#
# find(short_wait, "a[class=gnb_my]").click()
# # short_wait은 좀더 빨리 볼수있다.
# time.sleep(3)
# find(wait, "a#gnb_logout_button").click()

search = find(wait, "input[class=_searchInput_search_text_3CUDs]")
search.send_keys("로지텍마우스", "\n")
time.sleep(1)
# lowest_price = find(wait, "a[class=subFilter_sort__lhuHl]").click()  # 최저값
# time.sleep(5)
# 정규식으로도 값들을 가져올수있다.
# a[class="subFilter_sort__lhuHl"]
# a[class^="subFilter_sort__lhuHl"]

find(wait, "a[class^=basicList_link__]")
# 스크롤 내리는 방법
for i in range(8):
    chrome.execute_script("window.scrollBy(0,"+str((i+1)*1000)+")")
    time.sleep(1)
title = chrome.find_elements(By.CSS_SELECTOR,"div[class^=basicList_info_area__]")

print("---------------------------")
for titles in title:
    try:
        a = titles.find_element(By.CSS_SELECTOR,"button[class^=ad_]")
        continue
    except:
        pass
    print(titles.find_element(By.CSS_SELECTOR,"a[class^=basicList_link__]").text)
chrome.close()
