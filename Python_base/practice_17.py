# 집합 (set)
# 중복 안됨, 순서 없음
# intersection() 교집합과 동일한 결과
# & 교집합 
# | 합집합
# union() 합집합
# - 차집합
# difference() 차집합
# add() 추가
# remove() 지우다

my_set = {1,2,3,3,3}
print(my_set)


java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)

print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

#차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java-python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊어버림
java.remove("김태호")
print(java)
