def menu():  # 하나의 함수에는 하나의 기능을 넣는 것이 기본임
    print("오늘의 메뉴")
    print("제육볶음")
    print("내일의 메뉴")
    print("돈까스")


menu()


def add(num1, num2):
    '''숫자 두개(첫번째, 두번째)를 입력받아서 합쳐서 출력
    args
        num1 :
        num2 :
    '''  # 독스트링
    print(num1 + num2)


add(1, 2)  # 인자의 개수가 매개변수의 개수와 같아야 된다.


def add_text(text1, text2):
    '''문자열 두개(성, 이름)을 입력 받아서 합쳐서 출력
    arg
        text1 : 성을 받는 문자열
        text2 : 이름을 받는 문자열
    '''
    print(text1 + text2)


print(add_text("홍", "길동"))  # add에서 홍길동을 반환해서 이미 값이 없어서 print()가 출력되는
# 바람에 None이 출력됐음


def add_text(text1, text2):
    '''문자열 두개(성, 이름)을 입력 받아서 합쳐서 출력
    arg
        text1 : 성을 받는 문자열
        text2 : 이름을 받는 문자열
    '''
    text = text1 + text2
    return text


print(add_text("홍", "길동"))  # 반환값이 있어서 정상적으로 출력됐음
