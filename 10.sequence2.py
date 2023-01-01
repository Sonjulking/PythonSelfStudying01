# list[] tuple()

numbers = (1, 2, 3, 4)
nx = 1, 2, 3, 4  # 튜플 자료형은  괄호를 생략 가능
# 요소가 하나 일때는 콤마를 꼭 붙여야됌 .
# numbers = 1, #numbers = (1, )
# append extend insert 등 함수 사용 불가
print(type(numbers))
print(numbers.index(3))
print(numbers[3])
print("----------------------")

print(2 * numbers)

numbers = (1, 2, 3, (12, 32, 40))
print(numbers)

# 언패킹
numbers = (1, 2, 3)
number1 = numbers[0]
number2 = numbers[1]
number3 = numbers[2]

print(number1, number2, number3)

# 언패킹을 하면 이 코드를 간략하게 해줄 수 있음
numbers = (1, 2, 3)
number1, number2, number3 = numbers
print(number1, number2, number3)

# 변수가 너무 많으면 오류가 생김
numbers = 1, 2, 3, 4
number1, number2, *number3 = numbers
print(number1, number2, number3)

# 튜플에 값을 추가할 수 있는거처럼 보이게 할 수 있음.
numbers = 1, 2, 3, 4
print(numbers)
print(id(numbers))
numbers += 5, 6,
print(numbers)

# 메모리 주소를 확인해본다면? 두개가 서로 다름
print(id(numbers))

# 기존에 있던 튜플에 요소를 추가 한게 아니라 새로운 객체를 만들어서 참조함
