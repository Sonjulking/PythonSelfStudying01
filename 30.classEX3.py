class BreadMold:
    category = "빵"


bread1 = BreadMold()
bread2 = BreadMold()
bread3 = BreadMold()

# bread1 객체이름공간
bread1.price = 3000  # 새로운 속성을 추가함
# 새로운 속성을 추가하지만 클래스에 추가하는것이 아니라 다른 객체에 영향을 미치지 않음

# bread2 객체이름공간
bread2.category = "붕어빵"
# bread3 객체이름공간
bread3.category = "잉어빵"
# 네임스페이스(이름공간)가 따로 있음

# dir() 함수 =>이름공간에 있는 모든 속성을 리스트로 반환해줌

print(dir(bread1))  # 직접 지정해주지 않은 속성도 출력이 된다.
print(dir(bread2))
print(dir(BreadMold))
print(dir(str))
