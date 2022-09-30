s = 'apple'
print(s.find('p')) #find는 찾는 글자의 위치를 반환해줍니다.
arr = s.split('p') #split에 넣어준 값을 없애주고 list 형태로 돌려준다.
print(arr)



s='제 생일은 3월 입니다.'
print(len(s))
print(s.split('생일은 '))
print(s.split('월'))
pos = s.find('생일은 ')
pos += 4
print(s[pos:pos+1])
bd = s.split('생일은 ')[1].split('월')[0]
print(bd)