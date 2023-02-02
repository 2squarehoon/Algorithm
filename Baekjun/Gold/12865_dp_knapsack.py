# G5 평범한 배낭
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
graph = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        w = arr[i][0]
        v = arr[i][1]
        if j < w:
            graph[i][j] = graph[i-1][j]
        else:
            graph[i][j] = max(v+graph[i-1][j-w], graph[i-1][j])
print(graph[N][K])