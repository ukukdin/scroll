import re

from bs4 import BeautifulSoup as BS
import requests as req
import numpy as np
'''beautifulsoup 이란?
request :http 통신을 편하게
beautiful : html 통신을 편하게 해줍니다. 
사실상 beautifulsoup 을 쓰므로써 request를 직접적으로 잘 쓰지 않습니다. 

주요 기능 : 
html 문자열 파싱
html 노드 인식 및 편리한 기능들
parent,children,contents,descendants,sibling
string,strings,stripped_strings, get_text()
prettify
html attribute
'''
# url="https://naver.com"
# res = req.get(url)
# soup=BS(res.text,"html.parser")
# print(soup.title.string)


url="https://finance.naver.com/marketindex/exchangeList.nhn"
res = req.get(url)
soup=BS(res.text,"html.parser")
tds = soup.find_all("td")
names=[]
prices=[]
for td in tds:
    if len(td.find_all("a"))==0:
        continue
    names.append(td.get_text(strip=True))
for td in tds:
        if "class" in td.attrs:
            if "sale" in td.attrs["class"]:
                prices.append(td.get_text(strip=True))


names=np.transpose(names)
print(names)
prices = np.transpose(prices)
print(prices)

'''strip 은 벗겨낸다 즉 필요없는 값들을 없애준다 get_text(strip=True) 
    td.string 하면 큰 공백이 나온다ㅣ.
    td.strings ==제너레이터 패턴이라 for loop 을 돌려야한다. 
    for s in td.strings:
        print(s)
    for s in td.stripped_strings:
        print(s)  == 이거는 td.get_text(strip=True) 와 같은 값이 나온다. 
        numpy.transpose 는 list를 줄을 바꿔준다. 여기서는 7재쭐마다 바꿔주고있다. 
    '''
'''css select 로 위에 복잡하게 가져왔던 값들을 조금 더 단순하게 가져오게된다. '''
names=[]
for td in soup.select("td.tit"):
    names.append(td.get_text(strip=True))
prices=[]


for td in soup.select("td.sale"):
    prices.append(td.get_text(strip=True))

print(names)
prices=np.transpose(prices)
print(prices)