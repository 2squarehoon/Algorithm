# G4 테트로미노
import sys
input = sys.stdin.readline

def check(n):
    global ans
    if n > ans:
        ans = n
def ㅗ(a, b):
    for i in range(a+1, a+3):
        for j in range(b, b+3):
            cnt = arr[i][j] + arr[i-1][j] + arr[i+1][j] + arr[i][j+1]
            check(cnt)
    for i in range(a, a+3):
        for j in range(b+1, b+3):
            cnt = arr[i][j] + arr[i][j-1] + arr[i][j+1] + arr[i+1][j]
            check(cnt)
    for i in range(a+1, a+4):
        for j in range(b+1, b+3):
            cnt = arr[i][j] + arr[i][j-1] + arr[i][j+1] + arr[i-1][j]
            check(cnt)
    for i in range(a+1, a+3):
        for j in range(b+1, b+4):
            cnt = arr[i][j] + arr[i-1][j] + arr[i+1][j] + arr[i][j-1]
            check(cnt)

def dfs(i, j, idx, total): # ㅗ를 제외한 모든 모양은 첫 시작점에서 뒤로가지 않고 쭉 진행하는 모양이므로 dfs로 4번 이동한 값들로 구할 수 있다.
    if idx == 3:
        check(total)
    else:
        for n in range(4):
            ni = i+di[n]
            nj = j+dj[n]
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
                visited[ni][nj] = 1
                dfs(ni, nj, idx+1, total+arr[ni][nj])
                visited[ni][nj] = 0

N ,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
ans = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, arr[i][j])
        visited[i][j] = 0
for i in range(N - 3):
    for j in range(M - 3):
        ㅗ(i, j)
print(ans)