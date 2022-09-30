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
time.sleep(5)
#id 찾는법 beautifulsoup을 사용해서 찾기가 가능함.
wait = WebDriverWait(chrome,10)
el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[class=common_border]")))
print(el.text)
chrome.close()

'''






'''