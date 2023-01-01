def max_min_search(*args):
    max_num = args[0]
    min_num = args[0]

    for i in args:
        if i > max_num:
            max_num = i
        elif i < min_num:
            min_num = i
    return max_num, min_num
# numbers.sort(reverse=True) =>튜플이라 사용 불가능. 함수사용은 밑에있음!


print(max_min_search(15, 30, 4, 60, 7, 80, 32))

# 내장함수 사용 ㅋㅋㅋㅋ


def max_min_search2(*num):
    return max(num), min(num)


print(max_min_search2(15, 30, 4, 60, 7, 80, 32))
