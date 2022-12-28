# S1 회의실 배정
import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    start, end = map(int, input().split())
    lst.append((start, end))
lst = sorted(lst, key=lambda x: x[0])
lst = sorted(lst, key=lambda x: x[1])
ans = 0
last = 0
for s, e in lst:
    if s >= last:
        ans += 1
        last = e
print(ans)