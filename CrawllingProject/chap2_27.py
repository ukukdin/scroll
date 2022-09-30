from bs4 import BeautifulSoup as BS
import requests as req

url= "https://finance.naver.com/sise/lastsearch2.naver"
res = req.get(url)
soup = BS(res.text,"html.parser")
#
# for title in soup.select("a.tltle"):
#     print(title.get_text(strip=True))
for tr in soup.select("table.type_5 tr"):
    if len(tr.select("a.tltle"))==0:
        continue
    title = tr.select("a.tltle")[0].get_text(strip=True)
    price = tr.select("td.number:nth-child(4)")[0].get_text(strip=True)
    change = tr.select("td.number:nth-child(6)")[0].get_text(strip=True)
    print(title,price,change)


'''
일단, 크롬개발자 도구에서 html 을 볼때 개발자의 의도로 tbody 혹은 넣지 않아도 되는것들을 안넣을때 크롬개발자도구는
보기 좋은 코드를 위해서 임의로 태그들을 넣습니다. 그러므로 크롤링할때 생기는 오류들이 있습니다. 
td.number:nth-child() 에서 td의 number는 1~3개가 있지만 td의 순수한 순서를 따라야지만 값이 제대로 나옵니다.
예를 들어 


					<td class="no">1</td>
					<td><a href="/item/main.naver?code=005930" class="tltle">삼성전자</a></td>
					<td class="number">1.41%</td>
					<td class="number">56,700</td>
					<td class="number">
					
		이값에서 56.700의 값을 구하려면 td.number:nth-child(2) 가 아닌 td.number:nth-child(4) 
		즉 number의 상관없이 td의 순서에 맞게 넣어주셔야합니다. 
		
		if len(tr.select("a.tltle"))==0: continue는 tr.select 타이틀 길이가 0이면 건너뛰고 포문을 돌려주세요. 

'''