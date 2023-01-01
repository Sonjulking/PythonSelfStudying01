numbers = list(range(0, 10))

print(numbers)

numbers = list(range(-10, 0))

print(numbers)

numbers = list(range(-10, 0, 2))

print(numbers)

# range안에 수식도 입력가능

numbers = list(range(-10, 1+0, 2))

print(numbers)

# 나눗셈 연산은 실수형으로 반환 되기 때문에 '/' 이게 아니라 '//' 몫을 구해주는 연산자를 사용해야된다.
# 아니면 정수형으로 형변환을 시켜줘야된다. int(/)
