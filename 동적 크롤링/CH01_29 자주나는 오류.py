from selenium import webdriver
from selenium_stealth import stealth
import time
chrome = webdriver.Chrome("D:/chromedriver")
# 스텔스 기능으로 가끔 정적크롤링을 거절하는 사이트들을 위한 api입니다.
stealth(chrome,
        languages=["kr-KR","KR"],
        platform="win32",
        vendor="Google Inc.",)
url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"
chrome.get(url)
time.sleep(5)
chrome.quit()