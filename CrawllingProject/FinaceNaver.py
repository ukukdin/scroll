import requests as req
import re
url = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
res = req.get(url)

body = res.text
'''DOT
DOTALL 모든것을 검사해서 복사해 라는것
.* == 아무문자나 가져와 이고
.*? 가장 좁은 범위에 아무문자나 가져와'''
# r =re.compile(r"미국 USD.*?value\">(.*?)</", re.DOTALL)
r =re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)
captures = r.findall(body)
# pos = body.split('<span class="value">')[1].split('</span>')[0]

print(captures)
print("환율계산기")

for c in captures:
    print(c[0]+":"+c[1])
print()

usd = float(captures[0][1].replace(",",""))
print(usd)
won = input("달러로 바꾸길 원하는 금액(원)을 입력해주세요 : ")
won = int(won)
dollor = won/usd
dollor = int(dollor)
print(f"{dollor} 달러 환전 되었습니다. ")