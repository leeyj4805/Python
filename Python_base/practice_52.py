#예외처리
class BigNumberError(Exception): # 메세지를 가지고 있음
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg    
try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요:"))
    num2 = int(input("두 번째 숫자를 입력하세요:"))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1,num2))
    print("{0} / {1} = {2}".format(num1,num2, int(num1/ num2)))
    # 특정 에러를 발생시켜서 
except ValueError: # 이곳에 출력됨
        print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

except BigNumberError as err: #사용자가 정의한 에러가 나왔기 때문에 이 에러가 실행
        print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
        print(err)

finally:
    print("계산기를 이용해 주셔서 감사합니다.") #최종 예외처리 - 무조건 나옴