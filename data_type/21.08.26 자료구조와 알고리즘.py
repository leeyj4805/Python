# 자료구조와 알고리즘


# 3,2,7,8,4,5,1,6
# 1,2,7,8,4,5,3,6
# 1,2,3,8,4,5,7,6
# 1,2,3,4,8,5,7,6
# 1,2,3,4,5,8,7,6
# 1,2,3,4,5,6,7,8

# 선택정렬 (selection sort) O(N2)
# 버블정렬 (bubble sort) O(N*2)두개씩 비교 N,N-1...

# 퀵소트 (quick Sort) 기준을 두고 비교 
# 피벗을 랜덤으로 잡거나 중앙으로 잡거나 해야됨

# 시간복잡도가 길다

# T(N) =  2T(N/2) + N
# 2(2T(N/4)+N/2) + N
# 4T(N/4) + N + N
# 4T(N/4) + 2N
# 8T(N/8) + 3N....

# Nlog2 N

# Merge Sort (병합정렬)

# 3,2,8,1,4,5,7,6
# 3,2|8,1|4,5|7,6
# 32,81,45,76
# 23,18,45,67 ...

# 2 pointer - 포인터를 지정해서 2개 비교 후 정렬
# T(N) = T(N/2) *2 + N -> O(N)
# 메모리 할당을 위해 외부 메모리가 필요하다.

# sorted()..
# Radix Sort
# 3 1 9 2 2 4 5 6
