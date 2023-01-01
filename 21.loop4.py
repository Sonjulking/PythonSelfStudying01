i = 0

while True:
    print("{}번째 반복입니다.".format(i))
    i += 1
    if i > 10:
        break

# sum_ = 0
# while True:
#     num = int(input("정수를 입력해주세요.(0 입력시 종료) > "))
#     if num == 0:
#         print("종료했습니다.")
#         break  # break 밑에 코드는 전부다 실행되지가 않는다.
#     sum_ += num
#     print("현재 정수의 합은 {}입니다.".format(sum_))

numbers = [10, 200, 30, 400, 50]

for i in numbers:
    if i < 200:
        continue  # 여기서 다시 조건식 밖으로 돌아감
    print("{}은 200이상의 숫자입니다.".format(i))

numbers = [[1, 2, 3], [10, 20, 30]]

for i in numbers:
    print(i)
    for j in i:
        print(j)
        break  # 가장 가까운 반복문만 종료
