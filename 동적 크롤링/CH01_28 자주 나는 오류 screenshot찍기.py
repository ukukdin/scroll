from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os


options = webdriver.ChromeOptions()

options.add_argument("--headless")==True
options.add_argument("window-size=1120,1020")
options.add_argument("no-sandbox")

chrome = webdriver.Chrome("D:/chromedriver",options=options)
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)


def find_present(css):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,css)))

def finds_present(css):
    find_present(css)
    return chrome.find_elements(By.CSS_SELECTOR,css)
# 단수
def find_visible(css):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
# 복수
def finds_visible(css):
    find_visible(css)
    return chrome.find_elements(By.CSS_SELECTOR,css)

chrome.get("https://www.naver.com")

find_visible("input#query").send_keys("누리어시스템","\n")
a = find_visible("li[id=sp_nws_all1]")
# a.screenshot("./test1111.png")
# chrome.save_screentshot("./test.png")
# 윈도우 창의 사이즈를 늘리고 난후 body태그의안에 값들만 스크린샷으로 찍음

chrome.execute_script(""" 
    document.querySelector("li[id=sp_nws_all1]").setAttribute('style','border:10px solid red')
    """)

chrome.set_window_size(1000,10000)
body=finds_visible("body>img")
body.screenshot("./test3.png")


chrome.quit()