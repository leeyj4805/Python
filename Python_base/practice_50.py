# 에러 발생시키기

try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요:"))
    num2 = int(input("두 번째 숫자를 입력하세요:"))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1,num2, int(num1/ num2)))
    # 특정 에러를 발생시켜서 
except ValueError: # 이곳에 출력됨
        print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")