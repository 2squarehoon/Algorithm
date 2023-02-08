# G4 숨바꼭질 2
from collections import deque
N, M = map(int, input().split())
visited = [0]*100001
q = deque()
q.append(N)
distance = 0
ways = 0
while q:
    x = q.popleft()
    if x==M:
        distance = visited[x]
        ways += 1
        continue
    for nx in [x-1, x+1, x*2]:
        if 0<=nx<=100000:
            if not visited[nx] or visited[nx]==visited[x]+1:
                q.append(nx)
                visited[nx] = visited[x]+1
print(distance)
print(ways)