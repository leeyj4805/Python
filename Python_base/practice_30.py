# 지역변수와 전역변수
gun = 10 # 지역변수

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용 - 권장방법은 아님
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret (gun,soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
#checkpoint(2) # 2명기 경계 근무 나감
gun = checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))