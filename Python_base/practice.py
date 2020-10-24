#숫자 자료형

print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

#문자열 자료형

print("풍선")
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

# 불리언 자료형 (참과 거짓)

print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 변수
# 애완동물을 소개해 주세요
# str(age)- 정수형을 문자열로 바꿔줌
animal = "강아지"
name = "연탄이"
age = 4
hobby = "낮잠"
is_adult = age >= 3


print('우리집' + animal + '의 이름은' + name + '입니다.')
hobby = "공놀이" # 공놀이로 바뀌게 된다.
#print('name' + '는' + str(age) +'살이며' + hobby + '을 좋아합니다.')
print(name, '는', str(age), '살이며', hobby, '를 좋아합니다.')
print('name' + '는 어른일까요?' + str(is_adult))

# ''' 이렇게 하면 
# 여러문장이 주석처리가 
# 됩니다.
# ''' (ctrl + /)