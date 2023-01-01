weather = "맑음"
temperature = 20
print("오늘의 날씨는", weather, "기온은", temperature, "도 입니다.")  # sep, end
print("오늘의 날씨는 %s 기온은 %d도 입니다." % (weather, temperature))  # %를 이용하는 방법
print("오늘의 날씨는 {} 기온은 {}도 입니다.".format(weather, temperature))  # {}를 이용하는 방법

print("----------------------")

weather = "맑음"
temperature = 20
chance_shower = 33.5
print("오늘의 날씨는 %s 기온은 %d도 비가 내릴 확률은 %d%% 입니다." %
      (weather, temperature, chance_shower))
print("오늘의 날씨는 %s 기온은 %d도 비가 내릴 확률은 %f%% 입니다." %
      (weather, temperature, chance_shower))
print("오늘의 날씨는 %s 기온은 %d도 비가 내릴 확률은 %.1f%% 입니다." %
      (weather, temperature, chance_shower))

print("----------------------")

print("오늘의 날씨는 {} 기온은 {}도 비가 내릴 확률은 {} 입니다.".format(
    weather, temperature, chance_shower))  # 중괄호에 숫자와 요소숫자를 맞춰줘야됌. 요소가 중괄포보다 많으면
# 자동으로 순서대로 들어가지만 중괄호가 많으면 에러가 뜸.

print("오늘의 날씨는 {0} 기온은 {2}도 비가 내릴 확률은 {1} 입니다.".format(
    weather, temperature, chance_shower))

print("----------------------")

print("{}, {}".format(weather, temperature))
print("{:10}, {:10}".format(weather, temperature))  # 문자는 기본적으로 왼쪽 정렬이고,
# 숫자는 기본적으로 오른쪽 정렬
print("{0:s}, {1:d}, {1:f}, {1:o}, {1:x}".format(weather, temperature))

print("----------------------")

# 정렬하려면 <>^ 기호 사용
left = "left"
right = "right"
middle = "middle"

print("({2:>10s}),({1:^10s}),({0:<10s})".format(left, middle, right))
print("({2:!>10s}),({1:@^10s}),({0:#<10s})".format(left, middle, right))
print("({2:!>10.4s}),({1:@^10.3s}),({0:<10.2s})".format(left, middle, right))

# f-string
print("----------------------")
weather = "맑음"
temperature = 20

print(f"오늘의 날씨는 {weather}이며, 기온은 {temperature}도 입니다.")  # 엄청 간단함.
print(f"2곱하기 30의 결과값 = {2 * 30}")
