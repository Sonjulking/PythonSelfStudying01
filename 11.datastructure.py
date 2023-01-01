# dictonary 자료형
people = {  # 키는 중복이 없고, 딕셔너리나 리스트는 키값이 될 수 없다. 튜플은 가능함
    "name": "김세붕",  # 값은 중복이 가능하고 모든 자료형이 가능함
    "phone": "010-1010-2020"
}

print(people["name"], people["phone"])

books = {
    "Daniel Pink": ["파는것은 인간이다.", "언제 할 것 인가?"],
    "Eric Schdict": "새로운 디지털 시대"
}

print(books["Daniel Pink"])

# 키값으로 숫자와 논리형을 같이 쓸때는 주의해야 한다.

books = {1: "냉면", True: "고양이"}
print(books[1])  # True가 1로 계산되어서 True에 있는 문자열이 출력됐음
# False도 마찬가지라서 트루와 1 , 0과 False를 동시에 사용하는 것은 지양 해야된다.

coffee = {"Java": 2500, "Americano": 2500, "Latte": 3000}
# 요소를 수정
coffee["Java"] = 3000
print(coffee["Java"])

# 요소를 추가
coffee["Moca"] = 3000
print(coffee)

# 요소를 삭제
del coffee["Java"]
coffee.pop("Latte")
print(coffee)

# 키 값을 확인

print(coffee.get("Moca"))

# 요소를 확인
print(coffee.keys())
# 밸류를 확인
print(coffee.values())

# items() 키와 각 쌍을 튜플로 반환 해줌
print(coffee.items())

print("Moca" in coffee)
print("Moca Lattee" in coffee)
