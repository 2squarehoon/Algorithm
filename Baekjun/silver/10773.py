# S4 제로
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
stack = deque()
for _ in range(N):
    number = int(input())
    if number:
        stack.append(number)
    else:
        stack.pop()
print(sum(stack))