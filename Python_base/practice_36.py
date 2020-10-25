# with 데이터를 불러오기
# import pickle

# with open("profile.pickle","rb")as profile_file: 
#     #profile_file이라는 변수에 profile.pickle이라는 파일을 불러와서 넣음
#     print(pickle.load(profile_file))

# 데이터를 쓰기
# with open ("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# 데이터를 불러오기
with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())