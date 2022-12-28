# S3 구간 합 구하기 4

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst1 = [0]
cnt = 0
for i in range(N):
    cnt += lst[i]
    lst1.append(cnt)
for _ in range(M):
    a, b = map(int, input().split())
    print(lst1[b]-lst1[a-1])
