# S2 유기농 배추
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
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and arr[nx][ny]==1:
                visited[nx][ny] = 1
                q.append((nx, ny))

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1
    ans = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                bfs(i, j)
                ans += 1
    print(ans)
