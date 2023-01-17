# S1 미로 탐색
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y, 1)])
    visited[x][y] = 1
    while q:
        x, y, d = q.popleft()
        if x == N-1 and y == M-1:
            print(d)
            break
        else:
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and arr[nx][ny]==1:
                    visited[nx][ny] = 1
                    q.append((nx, ny, d+1))
bfs(0, 0)