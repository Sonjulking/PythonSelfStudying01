def division_if():
    num1 = input("첫번째 정수를 입력해주세요. > ")
    if num1.isdigit():  # isdigit메서드 활용
        num2 = input("두번째 정수를 입력해주세요. > ")
        if num2.isdigit() and num2 != 0:
            return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)}입니다.")
        else:
            print("0이 아닌 숫자로된 정수를 입력하세요.")
    else:
        print("숫자로된 정수를 입력하세요.")


def division_except():
    try:
        num1 = input("첫번째 정수를 입력해주세요. > ")
        num2 = input("두번째 정수를 입력해주세요. > ")

        return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)} 입니다.")
    except:
        print("0이 아닌 숫자로된 정수를 입력해주세요!!")


# 발생할 수 있는 에러 : valueError, zeroDivisonError, KeyboardInterrupt

def division_exception2():
    try:
        num1 = input("첫번째 정수를 입력해주세요. > ")
        num2 = input("두번째 정수를 입력해주세요. > ")

        return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)} 입니다.")
    except ValueError:
        print("숫자로된 정수를 입력해주세요!!")
    except ZeroDivisionError:
        print("제발 0을 입력하지 마세요!!")


help(ValueError)
help(ZeroDivisionError)


def division_except3():
    try:
        num1 = input("첫번째 정수를 입력해주세요. > ")
        num2 = input("두번째 정수를 입력해주세요. > ")

        return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)} 입니다.")
    except Exception as e:  # KeyboardIntterrupt는 Excpetion을 상속 받지 않기 때문에
        # KeyboardIntterrunpt도 예외 처치를 해주려면BaseException을 사용해줘야 한다.
        # as e를 써서 print(e)를 해주면 무엇때문에 오류가 나는지 알 수 있음.
        print(e)


def division_except4():
    try:
        num1 = input("첫번째 정수를 입력해주세요. > ")
        num2 = input("두번째 정수를 입력해주세요. > ")

        return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)} 입니다.")
    except Exception:
        print("오류가 발생했어요!")
    finally:  # 무조건 실행이 되는 구문임.
        print("정상적으로 나누기 함수가 호출 되었습니다.")


def division_except5():
    try:
        num1 = int(input("첫번째 정수를 입력해주세요. > "))
        num2 = int(input("두번째 정수를 입력해주세요. > "))
        result = num1 / num2
    except Exception:
        print("오류가 발생했어요!")
    else:
        print("정상적으로 나누기 함수가 호출 되었습니다.")
        return print("{}을 {}로 나눈 값은 {} 입니다.".format(num1, num2, result))
