class BreadMold:
    category = "빵"

    # __init__  생성자 메서드

    def __init__(self, category, price):
        self.category = category
        self.price = price
        print("빵을 만들었습니다.")

    # __str__ 메서드
    # 객체를 문자열로 반환했을때 출력값을 지정할 수 있는 메서드

    def __str__(self):
        return "{}의 가격은 {}원 입니다.".format(bread1.category, bread1.price)

    # __del__ 소멸자 메서드
    # 프로그램이 실행이 종료가 되면 객체가 사라지기 때문에 자동으로 실행됌
    # 레퍼런스 카운터가 0이되면 실행

    def __del__(self):
        print("빵이 없어졌습니다.")


bread1 = BreadMold("붕어빵", 3000)  # 생성했지만 더이상 사용을 안하기 때문에
# 소멸자 메서드가 사용됐음
bread1 = BreadMold("잉어빵", 4000)  # 변수가 같지만 변수는 객체가 아님
# 변수를 가져다 쓰는 이름!
# print("{}의 가격은 {}원 입니다.".format(bread1.category, bread1.price))

print(bread1)
