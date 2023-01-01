# 산술 연산자
print(10 + 2)
print(10 - 2)
print(10 * 2)
print(10 / 2)  # 파이썬의 나눗셈은 정수형이 아닌 실수가 나옴

print(type(10 / 10))

print(10 // 3)  # 몫을 구함
print(10 % 3)  # 나머지를 구함

# int()를 이용하여 정수로 변환
# 실수형, 논리형, 문자열이 정수형으로 변환 가능
print("----------------------")
print(int(123.993))
print(int(123.93323131))
print(int(123.0))

print(int(True))
print(int(False))

# print(int("212.44")) 이런식으로 문자열에 소수점이 있으면 형변환이 정상적으로 되지 않음.
print(type(int("2133")))

# float() 실수형
# 정수형, 논리형, 문자열
print("----------------------")
print(float(200))
print(float(3))

print(float(True))
print(float(False))

print(float("23.222"))
print(float("223"))  # int()와는 다르게 문자열안에 있는 정수도 변환 가능

# str()
# 모든 자료형
print("----------------------")
print(str(1223))
print(str(33.42))
print(str(True))
print(str(False))

# type으로 확인하면 str형으로 나옴.

print("----------------------")

# bool()
# 모든 자료형

# False
print(bool(0))
print(bool(0.0))
print(bool(""))

# True
print(bool(1))
print(bool(1.0))
print(bool("str"))
print(bool("1231"))

# 비교 연산자
print("----------------------")
a = 10
b = 20

# Equal sign ==

print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
print(a == b)
print(a != b)

# 논리형 자료
print("----------------------")

is_true = True
is_false = False
print(is_true > is_false)
print(is_true < is_false)

# 문자형 자료
print("----------------------")
print("Python" > "python")  # 문자형 자료에서 소문자가 대문자 보다 더 값이 큼. 이 명제는 False
print("12345" > "12344")
print("12.12" < "13.12")

# 복합대입연산자 (산술 연산자 + 대입 연산자)
# +=, -=, *=, /=, **=
print("----------------------")
today = 1230
today += 1  # today = today + 1
print(today)

# bool 자료형 연산
print("----------------------")
print(10 != 3)
print(10 == 10)

# and
print("----------------------")
print(True and True)
print(True and False)
print(10 > 3 and 3 < 5)
print(10 == 1 and 1 == 5)

# or
print("----------------------")
print(True or False)
print(False or True)
print(False or False)

# and 응용
print("----------------------")
print("a" and 10 > 3 and 0)  # 0이 반환
print("a" and 10 > 3 and True and False)  # False가 반환
print("a" and 10 > 3 and True and "참")  # "참"이 반환

# or 응용
print("----------------------")
print(0 or 0.0 or False or "a")  # a가 반환
print(0 or 0.0 or False or " ")  # " "이 반환

# and, or 연산자 우선순위
print("----------------------")
print(True or False and "참")  # and 연산이 or 연산보다 순위가 높음
print((True or False) and "참")

# not 연산자
# 결과를 반대로 뒤집어줌
print("----------------------")
print(not (True or False))
print(not True)
print(not (10 > 3))

# 연산자 우선순위
print("----------------------")
print(3 * 2 ** 2)
print((3 * 2) ** 2)

print("----------------------")
a = 10
b = 20
a, b = b, a + b
print(a, b)  # 연산자 우선순위때문에 20, 40이 아니라 20, 30으로 나옴.
