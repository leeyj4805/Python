# 표준입출력

print("Phthon","Java") # 띄어써서 출력
print("Phthon"+"Java") # 붙어서 출력

print("Phthon", "Java", "JavaScript", sep = " vs ") 
#Phthon vs Java vs JavaScript 

print("Phthon", "Java",sep = " , ", end = "?") # end 부분은 문장의 끝 부분을 결정
print("무엇이 더 재미있을까요?") 

import sys
print("Phthon", "Java", file = sys.stdout) # 표준 출력으로 출력됨
print("Phthon", "Java", file = sys.stderr) # 에러가 뜬다.
print("무엇이 더 재미있을까요?") 

# 시험 성적
scores = {"수학" : 0 , "영어": 50, "코딩":100}
for subject, score in scores. items():
    #print(subject,score)
    print(subject.ljust(8), str(score).rjust(4), sep= ":") #ljust 왼쪽정렬 # rjust 오른쪽 정렬

# 은행 대기순번표
# 001~003 ...
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3)) # zfill ~만큼의 크기 없으면 0

answer = input ("아무 값이나 입력하세요 :")
answer = 10
print(type(answer)) # 항상 문자열로만 저장된다.
print ("입력하신 값은" +answer+ "입니다.")