import requests as req

url = "https://api.imgur.com/3/image?client_id=546c25a59c58ad7"

# f = open("image.png","rb")
# img = f.read()
# f.close()

with open("image.png","rb") as f:
    img = f.read()

# 자동으로 클로즈 해주는 역할 위 3줄짜리랑 같다.

print(len(img))

res = req.post(url,files={
    "image":img,
    "type":"file",
    "name":"image.png",
})
print(res.status_code)
print(res.text)

# 200 -> 성공
# 400 - > 보내는사람
#500 -> 받는사람 잘못
link = res.json()["data"]["link"]
print(link)


# 클라이언트 파일은 서버에서부터 자바스크립트 파일로 고정된 문자로써 온다