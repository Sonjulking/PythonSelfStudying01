# super : 부모
# sub : 자식

class ParentRestaurant:
    price = 15000

    def __init__(self, name, menu, recipe):
        self.name = name
        self.menu = menu
        self.recipe = recipe

    def __str__(self):
        return "가게 이름 : {}, 가게의 메뉴 : {}, 메뉴의 조리법 : {}".format(self.name,
                                                              self.menu, self.recipe)

    def __del__(self):
        pass


class ChildRestaurant(ParentRestaurant):
    price = 20000  # 재정의, 오버라이드
    marketing = "온라인 마켓팅"  # 이건 재정의가 아님. 새롭게 추가한거니까(끄덕)

    def __init__(self, name, menu, recipe, marketing):  # 부모클래스의 생성자 메서드 재정의
        ParentRestaurant.__init__(self, name, menu, recipe)
        self.marketing = marketing

    def __str__(self):
        return super().__str__() + ", 마켓팅 방법은 : {}".format(self.marketing)
        # 부모객체를 참조할 때 super() 메서드 사용


restaurant_info = ChildRestaurant("자식의 가게", "붕어빵", "붕어빵을 굽는다.", "온라인")
print(restaurant_info)
print(restaurant_info.price)

print(issubclass(ChildRestaurant, ParentRestaurant))  # 자식클래스인지 판단해주는 메서드
print(issubclass(ParentRestaurant, ChildRestaurant))
print(issubclass(int, ChildRestaurant))
print(issubclass(ParentRestaurant, int))

# 하위클래스에서 상위클래스로는 접근 가능하지만 상위클래스에서 하위 클래스로는 접근이 불가능함
