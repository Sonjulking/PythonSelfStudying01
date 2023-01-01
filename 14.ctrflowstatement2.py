# # elif
# lunch = input("점심메뉴 (제육덮밥, 돈까스, 김밥) > ")

# if lunch == "제육덮밥":
#     print("제육덮밥")
# elif lunch == "돈까스":  # elif문은 if문이 없으면 동작을 하지않음
#     print("돈까스")
# elif lunch == "김밥":    # 전부다 if로 처리하면 if가 출력되고 else가 동작 하게됌
#     print("김밥")
# else:
#     print("굶는다")

# elif문을 사용하지 않았을 때의 case

number = 100

if number > 90:
    print("90보다 큰 수 입니다.")
if number > 80:
    print("80보다 큰 수 입니다.")
if number > 50:
    print("50보다 큰 수 입니다.")
else:
    pass

print("----------------------")

if number > 90:
    print("90보다 큰 수 입니다.")
elif number > 80:
    print("90보다는 작고 80보다 큰 수 입니다.")
elif number > 50:
    print("80보다는 작고 50보다 큰 수 입니다.")
else:
    pass

# elif문은 위에있는 조건식이 거짓일때만 실행하기 때문에 주의 해야함.


# and ,or 사용
# if문 여러조건을 동시에 판별
# 3의 배수이면서 짝수인수를 판별해주는 조건식

# number = int(input("정수를 입력해주세요. > "))

# if number % 3 == 0 and number % 2 == 0:
#     print("3의 배수이면서 짝수 입니다.")
# elif number % 3 != 0:
#     print("3의 배수가 아닙니다.")
# else:
#     print("짝수가 아닙니다.")

# 중첩 if문

number = int(input("정수를 입력해주세요. > "))

if number % 3 == 0 or number % 2 == 0:
    if number % 3 == 0 and number % 2 != 0:
        print("3의 배수 입니다.")
    elif number % 3 == 0 and number % 2 == 0:
        print("3의 배수이면서 짝수 입니다.")
    else:
        print("짝수 입니다.")
else:
    print("3의배수도 짝수도 아닙니다.")
