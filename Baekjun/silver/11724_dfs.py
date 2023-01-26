# S2 연결 요소의 개수
import sys
sys.setrecursionlimit(10000) # 파이썬 재귀제한때문에 제약조건 걸어줘야
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)
cnt = 0
for j in range(1, N+1):
    if not visited[j]:
        cnt += 1
        dfs(j)
print(cnt)