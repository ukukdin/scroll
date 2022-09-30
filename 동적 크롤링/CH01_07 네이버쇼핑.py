from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") #sandbox- 크롬은 tab마다 별개의 프로세스입니다.
# options.add_argument("headless") #크롬창을 안보이게 할 떄


chrome = webdriver.Chrome("D:/chromedriver",options=options)
chrome.get("http://naver.com")
chrome.get("https://shopping.naver.com")
chrome.back() #이전 페이지로 돌아간다.
chrome.forward() #한번 갔던 페이지는 값들이 넘어와서 그다음에 들어가질때는 빠르게 들어가진다.  #다음 페이지로 간다.
time.sleep(3)
chrome.close()