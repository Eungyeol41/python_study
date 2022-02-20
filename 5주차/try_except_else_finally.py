# try except 구문으로 예외를 처리합니다.
try:
    # 숫자로 변환합니다.
    number_input_a = int(input("정수 입력 >> "))

    # 출력합니다.
    print("원의 반지름 : ", number_input_a)
    print("원의 둘레 : ", 2 * 3.14 * number_input_a)
    print("원의 넓이 : ", 3.14 * number_input_a * number_input_a)
except:
    print("정수만 입력하기!!")
else:
    print("No Exception")
finally:
    print("§ 프로그램 종료!! Bye~ §")
