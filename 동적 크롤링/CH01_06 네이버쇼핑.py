from selenium import webdriver
import time

chrome = webdriver.Chrome("D:/chromedriver")
time.sleep(3)
chrome.close()