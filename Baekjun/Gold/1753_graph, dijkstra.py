# G4 최단경로
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
import heapq

V, E = map(int, input().split())
K = int(input())
graph = [[] * (V+1) for _ in range(V+1)]
inf = sys.maxsize
distance = [inf]*(V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        d, n = heapq.heappop(q)
        if distance[n]<d:
            continue
        for i in graph[n]:
            c = d+i[1]
            if c<distance[i[0]]:
                distance[i[0]] = c
                heapq.heappush(q, (c, i[0]))
dijkstra(K)
for i in range(1, V+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])