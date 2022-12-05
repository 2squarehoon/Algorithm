# B1 수 정렬하기 3
import sys
input = sys.stdin.readline

N = int(input())
# lst = []
# for _ in range(N):
#     lst.append(input().split()[0])
# lst.sort()
# for number in lst:
#     print(number)
# 시간초과

# 계수정렬
arr = [0]*10000
for _ in range(N):
    arr[int(input())-1] += 1
for i in range(10000):
    if arr[i]:
        for j in range(arr[i]):
            print(i+1)