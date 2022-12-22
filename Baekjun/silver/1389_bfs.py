# S1 케빈 베이컨의 6단계 법칙
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    visited = [0]*(N+1)
    q.append(x)
    visited[x] = 1
    while q:
        c = q.popleft()
        for i in range(1, N+1):
            if graph[c][i]==1 and visited[i]==0:
                q.append(i)
                visited[i] = visited[c]+1
    return sum(visited)

N, M = map(int, input().split())
ans = [0]*(N+1)
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
q = deque()
for j in range(1, N+1):
    ans[j] = bfs(j)

min_num = 99999999999999999
ans_idx = 0
for k in range(1, len(ans)):
    if ans[k] < min_num:
        min_num = ans[k]
        ans_idx = k
print(ans_idx)
