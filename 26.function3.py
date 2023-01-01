# 기본 매개변수
def add(num1, num2=20):  # 기본 매개변수는 일반 매개변수 앞에 나올 수 가 없음
    return num1 + num2


# print(add(10, 15))

# a, b = 20, 40


# def add(num1=a, num2=b):
#     return num1 + num2


# print(add())

a, b = 20, 40


def add(num1=a, num2=b):
    return num1 + num2


a, b = 5, 10  # 함수 에볼루션
# 함수가 정의 되는 시점에서 변수들을 평가를 하기 때문에
# 함수 정의 이후에는 변수를 수정해도 결과값이 변화가 되지 않음.
# 바뀐값으로 출력하고 싶으면 print(add(a,b))로 작성해야됌

print(add())


# 가변 매개변수
def add(num, *args):  # 가변 매개변수를 사용하려면 " * " 를 사용해야된다.
    # 가변 매개변수는 일반 매개변수 뒤에 와야된다.
    sum = num
    for i in args:
        sum += i
    print(sum)


add(10, 20, 30, 40)

# 가변매개변수를 인자로 받아서 반환을 해주면 튜플 형태로 반환해줌


def add(*args):
    return args


print(add(10, 20, 40, 50))

# 키워드 매개변수
# 키워드 = 특정값 형태로 {"키워드" : "특정값"} 반환


def star_player(**kwargs):  # 키워드 매개변수는 " ** "를 사용
    for i, j in kwargs.items():
        if "서장훈" in kwargs.values():
            print("저는 LG팬이라서 서장훈을 좋아했어요.")
        else:
            print("{}는 역시 {}지".format(i, j))


star_player(축구="손흥민", 야구="박용택", 농구="허재")
star_player(농구="서장훈")

# end = 이런 속성도 키워드 매개변수임

# 매개변수의 순서


def func_a(name, *args, address="한국", **kwargs):  # 일반 가변 기본 키워드 순
    print(name, args, address, kwargs)


func_a("홍길동", "옛날", "사람", address="한양", 직업="도둑")
