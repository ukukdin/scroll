import requests as req



url = 'https://webhook.site/9ea20ffc-8ec1-40ad-a3f0-bdfe3e78a3d9'
res = req.post(url,data={
    "name":"hi"
})
print(res.text)