# G4 트리의 지름
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1): # 트리 구현
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def dfs(x, w):
    for i in graph[x]:
        a, b = i
        if dist[a] == -1:
            dist[a] = w+b
            dfs(a, w+b)

dist = [-1] * (n+1)
dist[1] = 0
dfs(1, 0) # 1번 노드에서 가장 먼 곳 찾기
start = dist.index(max(dist)) # 가장 먼 노드 번호 찾기
dist = [-1] * (n+1)
dist[start] = 0
dfs(start, 0) # 찾은 노드에서 가장 먼 노드 번호 찾기

print(max(dist))