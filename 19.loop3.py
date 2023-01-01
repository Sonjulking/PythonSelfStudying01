# for 문

# for i in range(1, 10+1):
#     print(i)

# for i in "일이삼사오":
#     print(i)


fruits = ["사과", "딸기", "바나나"]
for i in fruits:
    print("과일 바구니에 \"{}\"가 들어있습니다.".format(i))

# 1부터 30까지의 수 중에서 3의 배수들의 합을 구하시오.
# 3의 배수는 어떻게 구하면 될까요?
sum = 0

for i in range(1, 30+1):
    if i % 3 == 0:
        print("{} + {} = ".format(sum, i), end="")
        sum += i
print(sum)

# 스텝을 이용한 방법
sum = 0
for i in range(3, 30+1, 3):
    print("{} + {} = ".format(sum, i), end="")
    sum += i
print(sum)

coffee = {"아메리카노": 2500, "라떼": 3000, "자바": 2500}

for i in coffee.items():
    print(i)

for i in coffee.values():
    print(i)

# enumerate 함수
fruits = ["사과", "딸기", "바나나"]  # 번호에 변수를 담고 싶을때 사용
for i in enumerate(fruits):
    print(f"{i[0]+1}번째 과일은 {i[1]}입니다.")

# 2차원 리스트
# for i in range(1, 3):
#     for j in range(1, 3):
#         print("첫번째 for문의 반복 {}번, 두번째 for문의 반복{}번".format(i, j))

list_2nd = [[1, 2, 3], ["a", "b", "c"]]

for i in list_2nd:
    print(i)
    for j in i:
        print(j)


# 3차원 리스트
# 3중 포문
list_3rd = [[[1, 2, 3], [4, 5, 6]], [[11, 12, 13], [14, 15, 16]]]

cnt1 = 0
cnt2 = 0
cnt3 = 0

for i in list_3rd:
    cnt1 += 1
    print("i의 {}번째 반복입니다.".format(cnt1))
    print(i)
    for j in i:
        cnt2 += 1
        print("j의 {}번째 반복입니다.".format(cnt2))
        print(j)
        for k in j:
            cnt3 += 1
            print("k의 {}번째 반복입니다.".format(cnt3))
            print(k)
print("i의 {}번째, j는 {}번째, k는 {}번째 반복입니다.".format(cnt1, cnt2, cnt3))
