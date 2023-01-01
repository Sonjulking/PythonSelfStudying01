# int(정수) 형

a = 5
b = -5
c = 0
print(type(a), type(b), type(c))

# float(실수)형 부동소수점 : 소수점 이하를 갖는 수

d = 5.5
e = -5.5
f = 0.0

print(type(d), type(e), type(f))

# 과학적 표기법
# 123456.7 = 1.234567 x 10 ^ 5 => 1.234567e5
g = 1.234567e5

print(g)

# complex 자료형
# 일반 수학에서의 복소수  a + bi
# 파이썬에서의 복수 a + bj


# text = 'String \'Data\' Type'
# 탈출문자
# \', \", \\, \n, \r, \t
# print(text)

text1 = "Python \'is\" Easy"
print(text1)
text2 = "Pytonh \\is Easy"  # 역슬래시를 두번쓰면 역슬래시 출력!
print(text2)
text3 = "Pytonh \nis Easy"  # 개행문자
print(text3)
text4 = "Java \rPython is Easy"  # 캐리지 리턴, Java 라는 문자열이 Python is Easy에 덮어 씌어짐.
print(text4)
text5 = "Py\tthon is Easy"  # 현재위치에서 8번째 뒤로 가는게 아니라 8번째 커서로 이동하는거임.
print(text5)
text6 = '''Python
is
Easy'''
print(text6)

t1 = "Python is Easy"
t2 = "and Powerful"

print(t1 + t2)
print(3 * t1)


a = 10
b = 20

print(a, b)
print(a, b, sep='@@')
print(a, b, end='개행문자 대신 사용합니다.')  # end 디폴트값으로 \n이 들어가 있음.
print("3번째 라인")
# 기본값은 이거랑 똑같음print(a, b)
# print()

# boolean 형

is_ture = True
is_false = False

print(is_false)
