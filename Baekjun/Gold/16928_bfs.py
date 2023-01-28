# G5 뱀과 사다리 게임
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
ladder = dict()
snake = dict()
for _ in range(N):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    snake[a] = b
visited = [0]*101
visited[1] = 1
cnt = [0]*101
q = deque([(1)])
def bfs():
    while q:
        x = q.popleft()
        for d in range(1, 7):
            nx = x+d
            if 1<=nx<=100 and not visited[nx]:
                if nx in ladder.keys():
                    nx = ladder[nx]
                if nx in snake.keys():
                    nx = snake[nx]
                if not visited[nx]:
                    visited[nx] = 1
                    cnt[nx] = cnt[x]+1
                    q.append(nx)
bfs()
print(cnt[100])