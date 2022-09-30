from bs4 import BeautifulSoup as BS
import requests as req
from user_agent import generate_user_agent,generate_navigator

# print(generate_user_agent(device_type='desktop'))
# print(generate_user_agent(os='win',device_type='desktop'))
# print(generate_user_agent(os=('mac','linux'),device_type='desktop'))
# navigator = generate_navigator()
# print(generate_navigator())
# print(navigator['platform'])

#
# url = "https://search.shopping.naver.com/search/all?query=%EC%95%84%EC%9D%B4%ED%8F%B0%20%EC%BC%80%EC%9D%B4%EC%8A%A4&cat_id=&frm=NVSHATC"
# res = req.get(url)
# soup = BS(res.text, "html.parser")
#
# arr = soup.select("ul.list_basis div>a:first-child[title]")
# for a in arr:
#     print(a.get_text(strip=True))

print('-------밑에부터는 쿠팡----------')

'''쿠팡에서 ad광고를 빼내는 방법'''
headers = { 'Accept-Language' : 'ko-KR,ko;q=0/9,en-Us;q=0.8,en;q=0.7,zh-TW;q=0.6,zh;q=0.5',
   'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Safari/537.36'
            ,'Accept-Encoding':'gzip'
}
# headers = {
# 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Safari/537.36'
#
# }
url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
print(url)
res = req.get(url, headers=headers)
# user-agent 는 사용자 기별을 식별하는데 사용하는 헤더입니다. 그래서 쿠팡 같은 경우는 헤더값을 줘야 조금 더 잘 잘동된다 이유는 봇으로 인식을 안하ㅏ기 위해서
soup = BS(res.text, "html.parser")

#
# arr = soup.select("div.name")
# for a in arr:
#     print(a.get_text(strip=True))
# 위에 꺼와 밑에 list comprehension 이랑 같지만 좀더 밑에 것이 syntax sugar 이다.
# arr = [a.get_text(strip=True) for a in soup.select("div.name")]
# print(arr)

# 광고 분석하기

# arr = [desc for desc in soup.select("div.descriptions-inner") if len(ads) == 0 : desc.select("div.name[0].get_text(strip=True)")]
bb =soup.select("div.descriptions-inner")

for desc in soup.select("div.descriptions-inner"):
    ads = desc.select("span.ad-badge")
    # if len(ads) == 0:
    #     print(desc.select("div.name")[0].get_text(strip=True))
    if len(ads) > 0:
        print("광고!")
    print(desc.select("div.name")[0].get_text(strip=True))