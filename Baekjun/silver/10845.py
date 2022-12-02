# S4 큐
import sys
from collections import deque

N = int(sys.stdin.readline())
Q = deque()
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        Q.append(order[-1])
    elif order[0] == 'pop':
        if Q:
            print(Q.popleft())
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

# https://codingpractices.tistory.com/entry/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%99%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EB%8C%80%EC%8B%A0-%ED%81%90-%EB%8D%B0%ED%81%AC-deque-%EB%A5%BC-%EC%93%B8%EA%B9%8C
# deque 사용