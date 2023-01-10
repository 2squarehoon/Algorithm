# S1 숨바꼭질
from collections import deque

def bfs(x, y):
    q = deque()
    q.append(x)
    while q:
        c = q.popleft()
        if c == y:
            print(dist[c])
            break
        for move in (c-1, c+1, c*2):
            if 0 <= move <= 100000 and not dist[move]:
                dist[move] = dist[c]+1
                q.append(move)

N, K = map(int, input().split())
dist = [0]*100001
bfs(N, K)