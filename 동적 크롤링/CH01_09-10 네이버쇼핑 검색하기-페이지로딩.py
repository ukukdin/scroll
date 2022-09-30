from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
'''웹페이지 로딩을 기다리는 이유는 원하는 데이터가 올라가기전에 값을 넣으면 에러가 난다. 

웹서버 요청 ->응답(http 을주는값) -> html 채우기 -> 그 후 css 불러오기 
(색,사이즈조절)->JS 실행(일반것과,마지막 자바스크립트 즉, css html 이 다 그려지고나서 들어오는 자바스크립트)-> 상품데이터 나옴
(js까지 실행되는대까지  로딩을 기다려주고 추가적인 데이터는 기다려주지 않는다. 

html 실행 후에 실행되는 onLoad, 자바스크립트는 온로드 체인 이라고(onLoad Chain) 순차적으로 js를 실행하는것(chaining 

time slepp 쓸때는 ->귀찮을때, (크롬에는 chrome.implicitly_wait() 이거는 크롬드라이버와 셀레니움이 쉬는것, 개발할때는 비슷한 느낌) 
우리가 필요하는 element 가 웹에 표시가 되어있는지를 표준점 삼아서 (
'''

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") #sandbox- 크롬은 tab마다 별개의 프로세스입니다.
# options.add_argument("headless") #크롬창을 안보이게 할 떄


chrome = webdriver.Chrome("D:/chromedriver",options=options)
# chrome.get("http://naver.com")
chrome.get("https://shopping.naver.com/window/main/pet-group?unionCategory=DOG")
WebDriverWait(chrome,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[class=homeServiceLinkBannerResponsive_home_service_link_banner_responsive__QsWwI]")))
# chrome.back() #이전 페이지로 돌아간다.
# chrome.forward() #한번 갔던 페이지는 값들이 넘어와서 그다음에 들어가질때는 빠르게 들어가진다.  #다음 페이지로 간다.
chrome.close()


