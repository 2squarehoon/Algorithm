# G5 숨바꼭질 3
from collections import deque
N, M = map(int, input().split())
visited = [0]*100001
distance = [-1]*100001 # 이동한 위치에 따른 시간
visited[N] = 1
distance[N] = 0
q = deque()
q.append(N)
while q:
    x = q.popleft()
    if x*2 <= 100000 and not visited[x*2]:
        q.appendleft(x*2) # 연산순위가 우선되어야하기때문에 appendleft
        visited[x*2] = 1
        distance[x*2] = distance[x]
    if x+1 <= 100000 and not visited[x+1]:
        q.append(x+1)
        visited[x+1] = 1
        distance[x+1] = distance[x]+1
    if x-1 >= 0 and not visited[x-1]:
        q.append(x-1)
        visited[x-1] = 1
        distance[x-1] = distance[x]+1
print(distance[M])