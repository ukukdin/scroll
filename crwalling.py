import requests as req

res = req.get("https://api.ipify.org/",headers={"fast":"campus"})
print(res.request.headers)
print(res.status_code)
print(res.text)
