# S2 트리의 부모 찾기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0]*(N+1)

def dfs(s):
    for i in graph[s]:
        if not visited[i]:
            visited[i] = s
            dfs(i)
dfs(1)
for j in range(2, N+1):
    print(visited[j])