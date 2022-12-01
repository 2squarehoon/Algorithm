# S5 요세푸스 문제 0

from collections import deque

N, K = map(int, input().split())
Q = deque()
ans = []
for i in range(1, N+1):
    Q.append(i)
while Q:
    for i in range(K-1):
        Q.append(Q.popleft())
    ans.append(Q.popleft())

print("<", end='')
print(', '.join(map(str, ans)), end='')
print(">")
