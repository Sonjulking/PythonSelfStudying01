# int(), str(), float(), bool(), tuple()...type()
# => 클래스임

number = 1
# 1이라는 데이터는 int 인스턴스(객체)로 사용한것이었음
text = "a"
numbers = (1, 2, 3, 4, 5, 6)

print(type(number))
print(type(text))
print(type(numbers))

number = 1
a = 1

# id() = 객체의 주소값을 반환

print(id(number))
print(id(a))
print(id(1))
# 얘네 3개는 같은 객체임!

# isinstance (인스턴스, 자료형)
# 인스터가 자료형에 속하나요?
number = 1
a = 1.0
print(isinstance(number, int))
print(isinstance(a, int))

# int(), str(), float(), bool()
# =>사실 형변환을 해주는게 아니라 새로운 객체를 생성해준 거임.

text1 = 12345
text2 = "12345"
print(id(text1), id(text2))
print(id(text1), id(int(text2)))
# 형변환이 아니라 새로운 객체를 생성해주는 것이라서 같은 text2이지만
# 전혀다른 주소값이 나옴
