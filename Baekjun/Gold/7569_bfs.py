# G5 토마토
import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
arr = []
for _ in range(H):
    arr.append([list(map(int, input().split())) for _ in range(N)])

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k]==1:
                q.append((i, j, k))

def bfs():
    while q:
        x, y, z = q.popleft()
        for d in range(6):
            nx, ny, nz = x+dx[d], y+dy[d], z+dz[d]
            if 0<=nx<H and 0<=ny<N and 0<=nz<M and arr[nx][ny][nz]==0:
                arr[nx][ny][nz] = arr[x][y][z]+1
                q.append((nx, ny, nz))
bfs()
ans = 0
for side in arr:
    for row in side:
        for col in row:
            if col==0:
                print(-1)
                exit(0)
        ans = max(ans, max(row))
print(ans-1)