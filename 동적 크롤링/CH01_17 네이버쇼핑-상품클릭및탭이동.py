from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

options = webdriver.ChromeOptions()
options.add_argument("window-size=1920,1200")
options.add_argument("no-sandbox")  # sandbox- 크롬은 tab마다 별개의 프로세스입니다.
# options.add_argument("headless") #크롬창을 안보이게 할 떄


chrome = webdriver.Chrome("D:/chromedriver")
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get("https://shopping.naver.com/")

def find(wait,css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,css_selector)))



login_button=find(wait, "a#gnb_login_button")

find(wait, "a#gnb_login_button").click()

input_id = find(wait, "input#id")
input_pw = find(wait, "input#pw")

pyperclip.copy("xkfcnwp")
input_id.send_keys(Keys.CONTROL, "v")  # 윈도우에서 사용하는 방식(컨트롤v 즉 복사해서 넣겠다.)
pyperclip.copy("dlsrnr12!")
input_pw.send_keys(Keys.CONTROL, "v", '\n')



search = find(wait, "input[class=_searchInput_search_text_3CUDs]")
search.send_keys("로지텍마우스", "\n")
time.sleep(1)
#
# for i in range(1):
#     chrome.execute_script("window.scrollBy(0,"+str((i+1)*1000)+")")



tt = chrome.find_elements(By.CSS_SELECTOR,"div[class^=basicList_title__] a[class^=basicList_link__]")[1].click()
# for t in tt:
#     print(t.text)
chrome.switch_to.window(chrome.window_handles[1])
find(wait,"a[class^=buyButton_btn_compare__]").click()
chrome.switch_to.window(chrome.window_handles[2])

# 마지막페이지
ttt=find(wait,"a[aria-haspopup=listbox]").click()
find(wait,"ul[role=listbox] li:nth-of-type(2)").click()
find(wait,"a[class=_2-uvQuRWK5]").click()
time.sleep(10)
chrome.quit()
#

# chrome.window_handles[0]은 먼저 열린탭 => 검색 결과탭
# chrome.window_handles[1]은 나중에 열린탭 =>
# print(chrome.window_handles)

