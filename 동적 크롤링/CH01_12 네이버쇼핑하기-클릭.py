from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") #sandbox- 크롬은 tab마다 별개의 프로세스입니다.
# options.add_argument("headless") #크롬창을 안보이게 할 떄


chrome = webdriver.Chrome("D:/chromedriver",options=options)
# chrome.get("http://naver.com")
chrome.get("https://swindow.naver.com/style/fashionbrand/list/category")

wait = WebDriverWait(chrome,10)
def find(wait,css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

search = find(wait, "input[class=_searchInput_search_text_3CUDs]")
search.send_keys("베이직 하우스\n")
time.sleep(3)
# button = find(wait,"button[class=_searchInput_button_search_1n1aw]")
# button.click()
# time.sleep(3)
'''가끔 로그인이 필요할때가 있으면 클릭으로만 안될수도있다. 그리고 단순히 클릭을 해주는 가 필용없다.
 그러할때 필요한것들은?
바로 엔터! \n 특수기호로 엔터와 같은것다. 유저와 브라우저의 상호작용을 크롬으로 흉내를 내는것과 같다. 
'''

chrome.close()

'''






'''