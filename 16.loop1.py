# print("Hello World\n" * 10)

# print(1)
# print(1+1)
# print(1+1+1)
# print(1+1+1+1)
# print(1+1+1+1+1)

# 반복문 while

# i = 0
# num = 10

# print("while 문")
# while i < num:
#     i = i + 1
#     print(i)

# print("if 문")
# if i < num:
#     i = i + 1
#     print(i)


# num = 0

# while num < 5:
#     num += 1  # 증감식의 위치가 중요 (결과가 달라짐!)
#     print(num)
# else:
#     print("값이 {}이상이므로 종료합니다.".format(num))

# 리스트를 사용한 while문

fruits = ["사과", "키위", "바나나", "사과", "바나나", "망고"]
print(fruits)
fruits.remove("사과")
print(fruits)  # 사과가 2개이지만 하나의 사과가 남아있음


fruits = ["사과", "키위", "바나나", "사과", "바나나", "망고"]
print(fruits)
remove_fruit = input("빼낼 과일을 입력해주세요 > ")

while remove_fruit in fruits:
    fruits.remove(remove_fruit)
print(fruits)
print("{}를 모두 제거 했습니다.".format(remove_fruit))
