# G5 토마토
import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            q.append((i, j))
def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and not arr[nx][ny]:
                arr[nx][ny] = arr[x][y]+1
                q.append((nx, ny))
bfs()
ans = 0
for row in arr:
    for col in row:
        if col==0:
            print(-1)
            exit(0) # 코드 강제종료
    ans = max(ans, max(row))
print(ans-1)