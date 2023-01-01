# class class는 변수,속성, 함수를 가질 수 있음
# 클래스는 붕어빵 틀 인스턴스는 붕어빵
class BreadMold:
    category = "크림빵"

    def make_bread(self):  # self 키워드 사용
        print("빵을 만들어 냅니다.")


# 객체이름 = 클래스 이름()
bread = BreadMold()
# 인스턴스(객체) 생성자

# 객체의 고유의 속성도 지정가능
bread.price = 3000

bread_choco = BreadMold()
bread_choco.category = "초코크림빵"

# "." 참조연산자. 참조 : 접근한다.
print(bread.category)

print("{}의 가격은 {}원 입니다.".format(bread.category, bread.price))
print(bread_choco.category)

# bread.make_bread() 파이썬에서는 함수를 호출할때 암묵적으로
# 인스턴스(여기서는 bread)를 전달해줌
# BreadMold.make_bread() takes 0 positional arguments but 1 was given
# =>인자를 받을게 없는데 한개가 전달이 되버려서 오류가 생김
# 해결하려면 self 키워드를 사용해야됌

bread.make_bread()  # self 키워드를 사용해서 오류를 해결함
