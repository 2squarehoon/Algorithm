# S2 색종이 만들기

import sys
input = sys.stdin.readline

def dfs(x, y, n):
    num = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != num:
                for k in range(2):
                    for l in range(2):
                        dfs(x+k*n//2, y+l*n//2, n//2)
                return
    if num==1:
        ans[1]+=1
    else:
        ans[0]+=1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0]
dfs(0, 0, N)
print(ans[0])
print(ans[1])