import re

s='hi'
print(re.match(r'hi',s))
#일치하는지에 대한것 '' 앞에 r붙이면 정규식으로 표현한다는 표식  span 은 어디서부터 매치가 되는것인지 알려주는것 .
print(re.match(r'h.',s))
print(re.match(r'..',s))
print(re.match(r'hi1*.',s))

s='color'
print(re.match(r'colou?r',s))
'''문자열 앞에 . 이 있으면 h 뒤에 아무거나 와도 된다.
.. 도 된다. . 하나만 넣어도 된다. 
*은 바로 앞에 글자가 0개 이상(즉 없을수도 있고 많을수도 잇다.) 즉 hi1111은 된다 hi11112는 되지 않는것이다. 이유는 * 뒤에 숫자가 0개 이상인경우 
+ 는 1이 1개 이상 잇어야한다. 
?는 없을수도 있다. ?을 매칭하고싶을때는 특수 기호는 특수 기호 무효화를 해주어야한다 \ <- 사용하여서 
[] = 이 중 아무거나  사용가능한것. 
'''
s='how are you?'
print(re.match(r'how are you\?',s))

w ='이 영화는 F등급 입니다'
print(re.match(r'이 영화는 [ABCF]등급 입니다',w))
# 패턴 매칭으로 해보기
''' findall
    match
    search
'''

print(w.split('이 영화는')[1].split('등급')[0])
print(re.findall(r'이 영화는 (.)등급 입니다.',w))