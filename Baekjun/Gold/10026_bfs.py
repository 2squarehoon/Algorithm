# G5 적록색약
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))

N = int(input())
arr = [list(map(str, input().rstrip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
normal = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            normal += 1
print(normal, end=' ')

visited = [[0]*N for _ in range(N)] # visited 초기화
for x in range(N): # 적록색맹의 경우 R,G 구분X
    for y in range(N):
        if arr[x][y] == 'R':
            arr[x][y] = 'G'
jjj = 0
for k in range(N):
    for l in range(N):
        if not visited[k][l]:
            bfs(k, l)
            jjj += 1
print(jjj)