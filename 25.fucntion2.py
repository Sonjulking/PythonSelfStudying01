# 지역변수(Loacal Variable), 전역변수(Global Variable)

# 지역변수
def jeju_potato():
    potato = "고구마"
    print(potato)


jeju_potato()

# 전역변수

potato = "고구마"


def jeju_potato():
    print(potato)


jeju_potato
print(potato)

# 전역변수와 지역변수를 섞어쓰면

potato = "감자"


def jeju_potato():
    # 함수에서 전역변수를 못가져와서 생긴 문제임
    # 사용하고싶으면
    # global potato  => global 키워드를 사용해줘야 한다.
    # print(potato)

    potato = "고구마"
    print(potato)


jeju_potato()

# 함수내에서는 지역변수를 사용하는게 좋음
# 함수를 쓸때 전역변수 사용하면은 계속 값이 바뀌어서 데이터의 흐름을 알아보기가 힘듬
