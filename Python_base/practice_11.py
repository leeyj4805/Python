# 문자열 포맷
# d는 정수의 의미를 가진다.
# %d는 문자열 포맷 코드
# %s 문자열 (string)
# %c 문자 1개(character)
# format 함수를 사용하여 포매팅을 할 수 있다.
# 중괄호는 숫자를 넣을 경우 순번에 맞게 출력이 된다.

print("a" + "b")
print("a" , "b")

# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")

# %s
print("나는 %s살입니다." % 20)

print("나는 %s색과 %s색을 좋아해요" %("파란","빨간"))
# 순서대로 들어간다.

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간",age = 20))

# 방법 4 
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")