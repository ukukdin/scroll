from bs4 import BeautifulSoup as BS
import requests as req
from user_agent import generate_user_agent, generate_navigator

headers = {'Accept-Language': 'ko-KR,ko;q=0/9,en-Us;q=0.8,en;q=0.7,zh-TW;q=0.6,zh;q=0.5',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/85.0.4183.101 Safari/537.36 '
    , 'Accept-Encoding': 'gzip'
           }
url = "https://finance.yahoo.com/most-active"
res = req.get(url, headers=headers)
soup = BS(res.text, "html.parser")

for tr in soup.select("table tbody tr"):
    title = tr.select("td:nth-child(1)")[0].get_text(strip=True)
    price = tr.select("td:nth-child(3)")[0].get_text(strip=True)
    change = tr.select("td:nth-child(5)")[0].get_text(strip=True)
    print(title, price, change)
