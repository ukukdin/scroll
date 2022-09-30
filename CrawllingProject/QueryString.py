'''
쿼리스트링 형식
?로 url과 구분된다.
url?querystring

값이름=값
adults=2
children=0

& 로 값들이 구분된다.
adults=2&children=0

배열은....
arr[]=1
arr[]=2
arr[]=3
arr[1,2,3,]
'''
import requests as req
import re

res = req.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B3%A0%EA%B5%AC%EB%A7%88")
html=res.text
print(html)