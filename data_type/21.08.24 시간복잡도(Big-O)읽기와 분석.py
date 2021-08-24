# 읽기와 분석 
# - 문제를 읽을 때 어떤 부분을 초점을 두고 읽어야 할까? (독해)
# - 문제의 조건들을 추상화하는 연습


# 코드의 실행 시간이 오래 걸리는가 -> 연산량

# 계산량은 어떤 값과 상관이 있을까? -> 입력

# 입력을 보고 시간을 계산할 수 있지 않을까?

# 대충 계산하자 => 점근적 표기법(Big O notation)

# 입력이 N일때 연산 횟수가 최악이 2N^2  + 4N이라면?
# N이 무한대로 커질 때 , 증가에 미치는 영향은 가장 큰 항만 필요하다

# O(N^2)

# O(1) 예시 

# 1부터 N까지 합을 구하시요

def sum_N(N): 
	return N*(N+1) // 2
(단순한 수식으로 표현 가능)


# O(N) 예시

# 길이 N수열에서 수 K 찾기

def search(1st, N, K): 
	for i in lst:
		if i == lst : return True
	return False

# * 최악의 경우 N번을 돌려봐야 함 확률적으로는 N/2번


# O(logN) 예시

# 정렬되어 있다는 정보가 있다면 어떨까? 0부터 9으로 가정하고 3을 찾는 과정을 생각하면...

# 0-9 중간 4

# 0-3 중간 1

# 23 중간 2

# 최종 결과 3


# 중복되는 과정을 어떻게 줄일 수 있을까 고민하는 과정이 필요 

def solution(n):
	ret = 0
	for i in range(1, n+1):
		ret += len(str(i))
	return ret
# -> 람다로 변환

# 수의 한번은 길이를 구해야 한다.

# 일의 자리수와 나머지로 나누기 


def num_len(n):
	ret = 0
	while n : 
		n/= 10
		ret++
	return ret:


# 읽기와 분석 외전
# - 입력과 초기화 팁
# (수,문자열/문자배열,배열)

num = int(input()) # 숫자면 형변환을 해야한다.<-문자열 (문장으로 받음)
string = input() # 문자열은 그대로 받는다.
char_lst = list(input()) # 각각의 알파벳으로 쪼갤 수 있다.

lst = list(map(int, input(),split())) # 수열은 map을 사용한다.

# map은 반복이 가능한 것을 넣겠다. 
# 문장이 들어왔을때 공백 단위로 쪼개고 
# 리스트에 원소를 int로 변환해주겠다. 
# char_lst 내용을 문자열로 만들고 싶으면 join메서드로 해야 한다.

# list 초기화 

lst_1d = [0 for _ in range(N)]
lst_2d = [[0 for _ in range(N)] for j in range(N)]

# - 에러 메세지 이해하기

# - 맞았습니다. -> 모든 테스트 케이스를 시간제한과 메모리 제한에 맞춰 통과
# - 틀렸습니다. -> 모든 테스트 케이스를 시간제한과 메모리 제한에 맞춰 탈락
# - 컴파일에러 -> 틀린 문법에 의해 생김(변수 오타,괄호 닫기,콜론)
# - 런타임에러 -> 돌아가는 과정상에 에러 (0으로 나누기, 잘못된 메모리 참조)
# - 메모리 초과 -> 메모리 터짐 더 효율적인 메모리 관리 필요
# - 시간초과 -> 시간 터짐 더 좋은 알고리즘 또는 최적화 필요
# - 출력 에러 -> 없는 경우도 존재 [디버깅 과정 코드] 확인 필요

# - 추상화와 기능분리 : 함수활용


TC = int (input()) # TC = test cases

while TC:
    N,M = map(int, input().split())
    #process
    print(answer)
    TC -= 1

def process():
    N,M = map(int, input.split())
    #process()
    return answer

for _ in range(int(input())):
    print(process())

    # Test Case가 많은 문제
    # 기능이 분리되는 문제 
    # 적절하게 함수로 분할하여 가독성
    # main 함수를 가볍게 하자

# i,j,k에 사다리 설치 

def check(i,j,k):
    pass
# result
def result():
    pass

# 간략한 psedo-code 느낌으로 작성
# 디테일한 부분은 함수를 만들며 수정

# 다중 반복문 사용 시, 수학적인 방법(몫과 나머지)을 이용하여 가볍게 변경

# - 가독성 : indent를 줄이자
# 두가지 방법을 추천 

# 1
def function2(x):
    if x: return True
    return False

# 2
def function3(x):
    return True if x else False

# - 명명법은 통일 

# - 카멜표기법 (함수)
# - 스네이크 표기법 (변수)
# - 파스칼 표기법 


# 수학(Math)



