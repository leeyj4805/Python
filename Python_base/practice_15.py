# 사전 자료형
# get() 함수는 x라는 키에 대응되는 Value를 돌려준다.

cabinet = {3: "유재석" , 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

print(cabinet[5])
# 5라는 키가 없기 때문에 오류가 생김
print("hi")