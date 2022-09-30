from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") #sandbox- 크롬은 tab마다 별개의 프로세스입니다.
# options.add_argument("headless") #크롬창을 안보이게 할 떄


chrome = webdriver.Chrome("D:/chromedriver",options=options)
wait = WebDriverWait(chrome,10)
short_wait = WebDriverWait(chrome,3)

chrome.get("https://shopping.naver.com/")
# login_button=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button")))
login_button=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button")))
# 
# 기대 조건을 presence_of_element를 쓰다보면 오류가 나는데 그 중하나는 준비가 다 되지 않는 상태에서 없어지는것.
print(login_button.text)
login_button.click()
time.sleep(3)
chrome.close()