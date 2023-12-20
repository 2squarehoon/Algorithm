# S5 회사에 있는 사람

from collections import deque

logs = dict()
n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    if b == "enter":
        logs[a] = b
    else:
        del logs[a]

logs = sorted(logs.keys(), reverse=True)

for a in logs:
    print(a)
