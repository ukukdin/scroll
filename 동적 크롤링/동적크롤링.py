from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

options = webdriver.ChromeOptions()
options.add_argument("no-sandbox")
chrome = webdriver.Chrome("D:/chromedriver", options=options)
wait = WebDriverWait(chrome, 10)
url = chrome.get("https://www.zentrade.co.kr/shop/goods/goods_list.php?&page=")

def find(wait, css_select):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_select)))
def find_visible(css):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

def finds_visible(css):
    find_visible(css)
    return chrome.find_elements(By.CSS_SELECTOR,css)

input_id = find(wait, "input[name=m_id]")
input_pw = find(wait, "input[name=password]")

pyperclip.copy("hitrend")

input_id.send_keys(Keys.CONTROL,"v") #윈도우에서 사용하는 방식(컨트롤v 즉 복사해서 넣겠다.)
pyperclip.copy("!qaz2wsx3edc")
input_pw.send_keys(Keys.CONTROL,"v")
input_pw.send_keys(Keys.CONTROL,'\n')
chrome.switch_to.window(chrome.window_handles[1])


result=[]

for page in range(1,2):
    url = chrome.get("https://www.zentrade.co.kr/shop/goods/goods_list.php?&page="+str(page))
    No = finds_visible('td[width="25%"] div:nth-of-type(1)')
    Name = finds_visible('td[width="25%"] div:nth-of-type(2) div:nth-of-type(2)')
    price = finds_visible('td[width="25%"] div:nth-of-type(3)')

    for aa in No,Name,price:
        for list in aa:
            list= result.append([No] + [Name] + [price])

chrome.quit()
