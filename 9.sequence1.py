# list [] 안에,
list_a = [1, 2, 3, 4]
list_b = ["a", "b", "c"]
list_c = [True, False]
list_d = [1, "a", True]

print(list_a)
print(list_b)
print(list_c)
print(list_d)

print("----------------------")
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
print(numbers[0])
print(numbers[3:5])
print(numbers[1:])
print(numbers[-3: -1])

print("----------------------")
list_lang = ["JAVA", "C", "Python", "Go"]
print(list_lang[0])
print(list_lang[0][1])
print(list_lang[2][2:4])

list_lang[1] = "C++"
print(list_lang)

list_lang[1:3] = ["C#", "Python3"]
print(list_lang)
list_lang[1:3] = ["C#", "Python2", "Python3"]
print(list_lang)

print("----------------------")
list_lang = ["JAVA", "C", "Python", "Go"]
print(len(list_lang))
print(list_lang)
# append() 리스트 맨 뒤에 있는 제일 마지막 인덱스(-1)에 새로운 요소를 추가

list_lang.append("Ruby")
print(list_lang)

# 주의점
list_a = [1, 2, 3]
list_lang.append(list_a)  # 이러면 리스트안에 리스트가 추가 되어버림
print(list_lang)

# 리스트가 아닌 요소를 추가하려면 extend()를 사용해야 된다.
list_lang.extend(list_a)
print(list_lang)
list_lang.extend("JavaScript")  # 주의점 : 문자열을 입력하면 문자 하나씩 들어감
print(list_lang)

# insert(index, data)

list_lang.insert(0, "R")
print(list_lang)

print("----------------------")

# 삭제하는 방법

# pop() pop은 삭제 한다기보다는 반환 해주는 느낌임. 반환해주고 삭제!
print(list_lang.pop())
print(list_lang)
print(list_lang.pop(0))
print(list_lang)

print("----------------------")
# remove() 요소를 직접적으로 지정하여 삭제 가능
list_lang.remove("Python")
print(list_lang)

# del()
del list_lang[1]
print(list_lang)
print("----------------------")

# list의 정렬
# sort()
numbers = [1000, 5000, 60, 100, 200, 3450]
numbers.sort()  # 오름차순으로 정렬
print(numbers)

# reverse() 리스트의 요소를 역순으로 변경
numbers = [1000, 5000, 60, 100, 200, 3450]
numbers.reverse()
print(numbers)

numbers = [1000, 5000, 60, 100, 200, 3450]
numbers.sort(reverse=True)  # 내림차순으로 정렬
print(numbers)
print("----------------------")

# 한글

names = ["홍길동", "고양이", "이승철"]
names.sort()
print(names)

# 영어
names = ["banana", "carrot", "apple"]
names.sort(reverse=True)
print(names)

compare_text1 = "apple"
compare_text2 = "banana"

print(compare_text1 > compare_text2)
print(compare_text1 < compare_text2)

# 컴퓨터가 똑똑해서 알아서 한글이나 영어를 오름차순 내림차순 해주는 것이 아니라
# 유니코드에 번호로 순서대로 등록이 되어있음!

# 문자의 코드 알기 ord, chr
print("----------------------")
print(ord("A"))
print(ord("a"))
print(ord("ㄱ"))
print(ord("ㅎ"))
print(ord("高"))

print(chr(66))
print(chr(98))
print(chr(12594))
print(chr(12623))

print("----------------------")

# in 연산자와 not in 연산자 요소의 값이 리스트 안에 있나용?
list_lang = ["JAVA", "C", "Python", "Go"]
numbers = [1, 200, 3, 50, 66, 7, 55, 9]

print(50 not in numbers)
print("C" in list_lang)
print("Java script" in list_lang)

print("----------------------")
text = ["가", "나", "다"]
print(text[0])
print(text[1])
print(text[2])

print(text[-1])
print(text[-2])
print(text[-3])

print(text[1:2])

print("----------------------")
# 2차원 리스트 인덱싱
td_number = [
    # 0   1   2
    [10, 20, 30],  # 0
    [1, 2, 3]      # 1
]
print(td_number)
print(td_number[1])
print(td_number[0][0])
print(td_number[1][2])
print("----------------------")
# 2차원 리스트 슬라이싱

print(td_number[0][0:2])
print(td_number[1][1:3])
