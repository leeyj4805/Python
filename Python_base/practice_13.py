# Q) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com 
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점 (.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                           (nav)     (5)             (1)        (!)       
# 예) 생성된 비밀번호 : nav51!



url = "http://naver.com"
my_str = url.replace("http://", " ") # 규칙 1
# replace () 문자열 변경시 사용하는 함수
#print(my_str)


my_str = my_str[:my_str.index(".")] # 규칙 2
#index()특정한 원소가 몇 번째에 처음으로 등장하는지 알려주는 것
# 처음부터 .직전까지 
# my_str[0:5] -> 0~5 직전까지 .(0,1,2,3,4)
#print(my_str)

passWord = my_str[:4] + str(len(my_str)) + str(my_str.count("e")) + "!" # 규칙 3
# 처음부터 4번째 직전까지 
# len() 길이를 구함
# count() 해당 값을 구함
print("{0} 의 비밀번호는 {1} 입니다.".format(url,passWord))
# format() 문자열의 대괄호 자리에 format 뒤의 괄호안에 들어있는 값을 하나씩 넣는다