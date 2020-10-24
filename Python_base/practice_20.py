# if else 만약 ~ 이 아니라면 ~이다.
# elif 조건을 검사해서 마음에 드는것을 고르는 것
# input() 키보드에 입력한 값을 받아들이는 명령어
# or 또는
# and ~이거나 ~일때 

weather = "미세먼지"
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요.")


# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")
    
temp = int (input("기온은 어때요?"))
if 30 <= temp: # 한가지 조건
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30: # 10도 이상이고 30도 미만
    print("괜찮은 날씨에요")
elif  0 <= temp < 10: # 0이상이면서 10 이하
    print("외투를 챙기세요")
else: # 나머지
    print("너무 추워요. 나가지 마세요")