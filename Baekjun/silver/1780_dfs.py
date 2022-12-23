# S2 종이의 개수

import sys
input = sys.stdin.readline

def dfs(x, y, n):
    num = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != num:
                for k in range(3):
                    for l in range(3):
                        dfs(x+k*n//3, y+l*n//3, n//3)
                return
    if num==-1:
        ans[0]+=1
    elif num==0:
        ans[1]+=1
    else:
        ans[2]+=1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0, 0]
dfs(0, 0, N)
for n in ans:
    print(n)