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
options.add_argument("no-sandbox")  # sandbox- 크롬은 tab마다 별개의 프로세스입니다.
# options.add_argument("headless") #크롬창을 안보이게 할 떄


chrome = webdriver.Chrome("D:/chromedriver", options=options)
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get("https://shopping.naver.com/")
def find(wait, css_select):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_select)))


# login_button=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button")))

find(wait,"a#gnb_login_button").click()


# visibility 는 주소의 엘레멘트가 보여지면 실행하라는 구문이다. 위의 presence는 존재하면 이라는것이기에 visibility 를 사용할때는 페이지가 로딩이 되어서 보여지는 형태가 되고난뒤다.
# 기대 조건을 presence_of_element를 쓰다보면 오류가 나는데 그 중하나는 준비가 다 되지 않는 상태에서 없어지는것.
# print(login_button.text)
# login_button.click()

# pyperclip(클립보드)에서 아이디를 복사하고  이것으로 입력을 붙여넣기 한다는것.


input_id = find(wait, "input#id")
input_pw = find(wait, "input#pw")

pyperclip.copy("xkfcnwp")
input_id.send_keys(Keys.CONTROL,"v") #윈도우에서 사용하는 방식(컨트롤v 즉 복사해서 넣겠다.)
pyperclip.copy("dlsrnr12!")
input_pw.send_keys(Keys.CONTROL,"v",'\n')
# input_pw.send_keys('\n')
# send_keys로 쓰게 되면 네이버에서는 영수증 리뷰로 인한 로그인이 안된다. pyperclip은 순차적으로 실행값 위에 넣어야함
# 한번에 다 적어놓으면 순서대로 읽기때문에 값이 달라진다.

# input_pw.send_keys("dlsrnr12!")

chrome.close()
