# 구구단 퀴즈
# 2단부터 9단까지 = 8번반복
# 1부터 9까지 = 8번 반복

print("2단부터 9단까지 구구단 출력")
for i in range(2, 9+1):
    print("{} X 1 = {}".format(i, i))

for j in range(1, 9+1):
    print(j)

for i in range(2, 9+1):
    for j in range(1, 9+1):
        print(f"{i} X {j} = {i * j}", end="\t")
print()
