# S4 요세푸스 문제
import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
people = deque()
ans = []
for i in range(1, N+1):
    people.append(i)

while people:
    for _ in range(K-1):
        people.append(people.popleft())
    ans.append(people.popleft())

print(str(ans).replace('[', '<').replace(']', '>'))
