#파일 입출력

# 출력
score_file = open("score.txt","w",encoding="utf8") 
print("수학 : 0",file = score_file)
print("영어 : 50",file = score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") 
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# 읽어오기
score_file = open("score.txt","r",encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

#읽기 방법
score_file = open("score.txt","r",encoding="utf8")
while True: # 무한 루프 (반복문)
    line = score_file.readline() # 읽어오기
    if not line: # 라인이 없다면
        break # 반복문 탈출
    print(line, end="") # 출력
score_file.close() #닫기

# 리스트로 처리 방법
score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines: # 리스트에 있는 내용들을 하나씩 가지고 옴
    print(line, end="")

score_file.close()



