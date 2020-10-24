# 튜플

menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스") - 오류가 남 (튜플이 없기 때문)

name = "김종국"
age = 20
hobby = "코딩"
print(name,age,hobby)

#튜플 - 리스트와 비슷하지만 생성,삭제,수정이 불가능
name,age,hobby = ("김종국" , 20 , "코딩")
print(name,age,hobby)