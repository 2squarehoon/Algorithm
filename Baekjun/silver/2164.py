# S4 카드2
import sys
from collections import deque

N = int(sys.stdin.readline())
lst = [i for i in range(1, N+1)]
Q = deque(i for i in range(1, N+1))
while len(Q) > 1:
    Q.popleft()
    Q.append(Q.popleft())
print(Q[0])