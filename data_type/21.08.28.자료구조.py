# 자료구조

# 추상화,재사용성,효율성

# stack

# 쌓다. 접시닦이 닦고 가지고 가기


# Queue

# push 또는 pop
# First In, Last Out  = FILO

# Array에서 하면 됨

# First In, First Out = FIFO

# 필요없는 부분의 메모리를 줄이기 위해 사용한다.

# deque = Stack + Queue

# From colletions import deque


# 11866 요세푸스 순열

from collections import deque
N, k = map(int , input().split())

dq = deque(range(1, N+1))
ans = list()

while len(dq):
    dq.rotate(-k+1)
    ans.append(dq.popleft())

print(f"<{str(ans)[1:-1]}>")
# 3,6,2,7,5,1,4

apple = 'apple'
print(f'{apple}')

# 출력하는 방법

