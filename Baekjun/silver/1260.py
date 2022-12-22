# S2 DFS와 BFS
import sys
input = sys.stdin.readline
from collections import deque

def dfs(x):
    visited1[x] = 1
    ans1.append(x)
    for i in range(1, N+1):
        if visited1[i]==0 and graph[x][i]==1:
            dfs(i)

N, M, V = map(int, input().split())
visited1 = [0]*(N+1)
visited2 = [0]*(N+1)
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
ans1 = []
ans2 = []

dfs(V)
visited2[V] = 1
Q = deque([V])
while Q:
    c = Q.popleft()
    ans2.append(c)
    for i in range(1, N+1):
        if visited2[i]==0 and graph[c][i]==1:
            Q.append(i)
            visited2[i] = 1
print(*ans1)
print(*ans2)