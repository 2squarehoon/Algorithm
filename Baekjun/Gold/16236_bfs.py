# G3 아기 상어
import sys
input = sys.stdin.readline
from collections import deque

def fish(x, y, size):
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    temp = []
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if arr[nx][ny] <= size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cx][cy]+1
                    if arr[nx][ny] < size and arr[nx][ny] != 0:
                        temp.append((nx, ny, distance[nx][ny]))
    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1])) # 거리, y축, x축 순으로 정렬

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
size = 2
for i in range(N): # 상어위치
    for j in range(N):
        if arr[i][j] == 9:
            x, y = i, j
cnt = 0
ans = 0
while True:
    shark = fish(x, y, size)
    if not len(shark):
        break
    nx, ny, dist = shark.pop()
    ans += dist
    arr[x][y], arr[nx][ny] = 0, 0
    x, y = nx, ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
print(ans)