# input()  # 입력을 받아줌

# text1 = input("성을 입력해주세요.")
# text2 = input("이름을 입력해주세요.")
# print(text1 + text2)

# number1 = input("첫번째 정수를 입력해주세요 >")
# number2 = input("두번째 정수를 입력해주세요 >")
# print(number1 + number2)  # 숫자가 문자열로 변환되어 저장됐음

# number1 = input("첫번째 정수를 입력해주세요 >")
# number2 = input("두번째 정수를 입력해주세요 >")
# print(int(number1) + int(number2))  # 숫자가 문자열로 변환되어 저장됐지만 다시 정수형으로 변환

# 입력받을때부터 정수형으로 받아줌. 정수뿐만 아니라 실수형도 가능
# number1 = int(input("첫번째 정수를 입력해주세요 >"))
# number2 = int(input("두번째 정수를 입력해주세요 >"))
# print(number1 + number2)  # 숫자가 문자열로 변환되어 저장됐음

# if 문
# if True:
#     print("실행할 문장입니다.")  # 파이썬 if문은 들여쓰기가 굉장히 중요함
#     # 스페이스 4칸을 추천


# weather = "비"

# if weather == "비":
#     print("우산 챙겨!")


# study_time = int(input("오늘의 공부시간을 입력해주세요. >"))
# # 만약에 오늘 공부할 시간이 3시간 이상이라면 파이썬 공부

# if study_time >= 3:
#     print("오늘은 파이썬 공부 합시다~")

# # 만약에 오늘 공부할 시간이 3시간 미만이라면 오늘은 놀자

# if study_time < 3:
#     print("오늘은 시간이 별로 없으니까 놀자!")


# 만약에 오늘 공부할 시간이 3시간 이상이고
# 6시간이하라면 파이썬 공부
# study_time = int(input("오늘의 공부시간을 입력해주세요. >"))
# if study_time >= 3 and 6 >= study_time:  # => and 연산자를 안쓰고 6 >= study_time >= 3 으로도 쓸 수 있음
#     print("오늘은 파이썬 공부 합시다~")

# if study_time < 3:
#     print("오늘은 시간이 별로 없으니까 놀자!")

# else문!

# odd = input("정수를 입력해주세요. >")
# # print(odd[-1] == "1")

# if odd[-1] == "1" or odd[-1] == "3" or odd[-1] == "5" or odd[-1] == "7" or odd[-1] == "9":
#     print("입력하신 정수는 홀수 입니다.")

# 효율적으로 짜보기
# odd = int(input("정수를 입력해주세요. >"))
# if odd % 2 == 1:
#     print("입력하신 정수는 홀수 입니다.")
# else:
#     print("입력하신 정수는 짝수 입니다.")

# 주민번호로 성별 구분하기
# 13자리중에서 7번째 숫자를 판별
# 123456-1234567
number = input("주민번호를 입력해주세요. >")
odd = int(number[7])

if odd % 2 == 0:  # 짝수라면
    print("여자")
else:  # 짝수가 아니라면... 홀수라면!
    print("남자")
