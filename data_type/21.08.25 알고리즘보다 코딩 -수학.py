# 알고리즘보다 코딩 -수학

# 컴퓨터의 모든 수는 2진수로 저장
# 우리는 모든 수를 10진수로 인식
# 숫자로 구성된 문자열을 N진법에 맞게 변환하기 위해서는?

def stoi(s,n):
    ret = 0
    l = len(s)
    for i in range(l):ret += int(s[i])*n**(l-i-1)
    retrun ret

# 이론적으로 각자리수 *N의 거듭제곱의 합으로 나올 수 있습니다.    
# 더 간단한 방법

def stoi(s,n):
    ret = 0
    l = len(s)
    for i in range(l):ret * n + int(i)
    retrun ret

# 조건문 + N진수 변환 방법으로 해결 가능

def pow_custom(a,b):
    ret = 1
    while b:
        if b % 2 == 1: ret *= a
        a = a*a
        b //=2
    ret ret

# 모듈러를 하는것이 시간복잡도 면에서 더 빠르다.

def pow_custom(a,b, mod):
    ret = 1
    while b:
        if b % 2 == 1: ret = ret * a % mod
        a = a*a % mod
        b //= 2
    return ret

# 최대공약수 : 공통적인 약수 중 최댓값 최대공약수가 1이면 서로소
# 최소공배수 : 공통된 배수 중 최솟값 
# LCM(A,B) = A x B/ GCD(A,B)


# 1부터 체크하는 방법

def gcd(a,b):
    ret = 0
    for i in range(min(a,b)):
        if a % i == 0 and b % i == 0:
            ret = i
    return ret

 # min(a,b)부터 체크

def gcd(a,b):
    for i in range(min(a,b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

# 유클리드 호제법? - 최소공배수와 최대공약수 구하는 공식
# 다항식
# GCD(A,B) = GCD(B,A%B)

def gcd (a,b): 
    return b if a%b == 0 else gcd (b,a%b)


# 소인수분해
 
def isPrime(N):
    for i in range(2,N):
        if N % i == 0: return False
    return True

# 2부터 N-1까지 체크 O(N)

def isPrime(N):
    i = 2
    while i*i <= N:
        if N % i == 0: return False
        i += 1
    return True  

# 2부터 sqrt(N)까지 체크 O(sqrt(N)) - 중간수까지 체크 (많이 쓰임)

# 에라토스테네스의 체 ( n의 배수로 지운다.)
# N까지의 소수를 구하기 위해서는 sqrt(N)까지의 소수를 이용하면 가능하다.


def era(N):
    ck, p = [False for _ in range(N+1)], []
    for i in range(2, N+1):
        if ck[i] == True : continue
        p.append(i)
        for j in range(i*i, N+1, i):
            ck[j] = True
    return ck, p
    

# 분할정복  - 문제를 분해할 수 있을까? (재귀함수 활용)

# 하노이탑

# 1. 마지막 판이 이동하기 위해서는 나머지 모든것이 한 곳에 있어야 한다.
# 2. 그렇다면 N개중 N-1개를 기둥 2에 보내는 것이 우선이다.
# 3. N번째 기둥을 3번에 보내고
# 4. N-1개의 기둥을 다시 기둥 3에 보낸다.
# 5. 기둥 1에서 2로 보내는 과정과 2에서 3으로 보내는 과정은 사실 같다.


# F(N) = 2XF(N-1)+1    F(1)= 1

# 하노이탑 공식

def hanoi(st, ed, sz):
    if sz == 1: return print(st, ed)
    hanoi(st, 6-st-ed, sz-1)
    print(st, ed)
    hanoi(6-st-ed, ed, sz-1)

n = int(input())
print(2**n-1)
hanoi(1,3,n)

# 재귀함수를 설계할 때 최소 조건 / 탈출조건을 분명하게 
# 분할 정보에 사용하기 위해서는 줄어든 문제 조건을 표현할 parameter가 필요
