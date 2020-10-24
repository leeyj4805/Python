# 출석번호가 1~4 앞에 100을 붙이기로 함 -> 101~104
students = [1,2,3,4,5]
print(students)

students = [i + 100 for i in students]
# i 에 100을 더한 값을 더하는데 students 리스트에 들어있는 값을 활용한다.
print(students)

# 학생 이름을 길이로 변환 -len
students = ["Iron man","Thor","I am groot"]
students = [len(i) for i in students] # 반복문
print(students)

# 학생이름을 대문자로 변환 - upper()

students = ["Iron man","Thor","I am groot"]
students = [i.upper() for i in students]
print(students)
