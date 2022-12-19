# S3 바이러스
import sys
input = sys.stdin.readline
N = int(input())
visited = [0]*(N+1)
graph = [[] for _ in range(N+1)]
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
# dfs
def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if visited[i]==0:
            dfs(i)
dfs(1)
print(sum(visited)-1)

# bfs
from collections import deque
visited[1] = 1
Q = deque([1])
while Q:
    c = Q.popleft()
    for i in graph[c]:
        if visited[i]==0:
            Q.append(i)
            visited[i] = 1
print(sum(visited)-1)
