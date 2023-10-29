# B3 공 넣기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [0]*N
for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        lst[x] = k
print(*lst)