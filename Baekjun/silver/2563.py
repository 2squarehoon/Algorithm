# S5 색종이

import sys
input  = sys.stdin.readline
N = int(input())
lst = [[0]*100 for _ in range(100)]
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            lst[i][j] = 1
ans = 0
for k in range(100):
    for l in range(100):
        ans += lst[k][l]
print(ans)