python = "Python is Amazing"

print(python.lower())
# 소문자로 출력
print(python.upper())
# 대문자로 출력
print(python[0].isupper())
# 파이썬의 변수의 값이 대문자라면 
# 출력이 된다.
print(len(python))
# 길이를 구함
print(python.replace("python","Java"))
# replace () 문자열 변경시 사용하는 함수

index = python.index("n")
print(index)
#index()특정한 원소가 몇 번째에 처음으로 등장하는지 알려주는 것
index = python.index("n", index + 1)
#index()특정한 원소가 몇 번째 + 1에 처음으로 등장하는지 알려주는 것
print(index)

print(python.find("n"))
# find() 찾다 

print(python.find("java"))
# 값이 없을때는 -1이 나옴

print(python.index("java"))
# 오류가 나옴

print(python.count('n'))
# n이 몇번째 나오는지 알려주는 것
