a = 100
b = 200

print(a)
# del b  # 변수를 삭제
print(b)

c, d = 100, 200  # 변수 여러개 지정
c, d = d, c + d  # +가  =보다 우선순위가 높다.
print(c, d)


text = 'Welcom to Python'
print((text + "\n") * 10)

# 이름, 핸드폰 번호, 거주지 :
name = '고강찬'
phone_Number = '010-9221-1669'
home_Adress = '서울시 강북구'

print(name)
print(phone_Number)
print(home_Adress)
