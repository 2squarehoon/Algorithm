# S4 덱
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Q = deque()
for _ in range(N):
    order = input().split()
    if order[0] == 'push_back':
        Q.append(order[1])
    elif order[0] == 'push_front':
        Q.appendleft((order[1]))
    elif order[0] == 'pop_front':
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if Q:
            print(Q.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(Q))
    elif order[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)
