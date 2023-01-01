text = "www.GOOGLE.com"

print(len(text))  # len 메서드는 요소의 개수를 반환해줌.

print("----------------------")

txt_capitalize = text.capitalize()  # 첫글자를 대문자로 변경해줌.

print(txt_capitalize)

print("----------------------")

txt_upper = text.upper()  # 문자열 전체를 대문자로 변경
txt_lower = text.lower()  # 문자열 전체를 소문자로 변경

print(txt_upper)
print(txt_lower)

print("----------------------")

# count, find , index

g_cnt = text.count('G')  # 갯수
print(g_cnt)
g_cnt = text.count('GO')
print(g_cnt)
g_cnt = text.count('X')
print(g_cnt)

print("----------------------")

g_find = text.find('G')  # 위치
print(g_find)
g_find = text.find('G', 5)  # 5번째 이후 G 위치
print(g_find)

print("----------------------")

g_idx = text.index('G')
print(g_idx)

g_find = text.find('X')
# g_idx = text.index('X')
print(g_find)  # 없으면 -1 출력
# print(g_idx) find와 index의 가장 큰 차이점 ! 인덱스는 값이 없으면  밸류에러가 발생함.
# 그래서 있는지 없는지 모르면 find를 쓰는게 좋음

print("----------------------")
# x 역순으로 찾아주기
gr_find = text.rfind('G')
gr_index = text.rindex('G')

print(gr_find)
print(gr_index)

print("----------------------")
# 문자열 치환
text_naver = text.replace("GOOGLE", "NAVER")
print(text_naver)

print("----------------------")

# 문자열을 구분자로 나누어줌

print(text.split('.'))  # . 이 있을때마다 구분해줌.
print(text.split('OO'))


# 좌우 공백을 없애주는 메서드
print("----------------------")
text = "                 www. GOOGLE .com                    "
print(text)
stp = text.strip()  # 문자열 사이에 있는 공백을 없애주지는 못함
print(stp)
print("----------------------")
lstp = text.lstrip()  # 왼쪽 공백
rstp = text.rstrip()  # 오른쪽 공백
print(lstp)
print(rstp)
