# continue와 break

absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1,11): # 1~10
    if student in absent:
        continue # 더이상 그 이후 문장을 실행하지 않고 반복문
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 반복문이 있든 없든 문장을 탈출함
    print("{0}, 책을 읽어봐".format(student))