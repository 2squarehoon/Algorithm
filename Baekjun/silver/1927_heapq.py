# S2 최소 힙
import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    x = int(input())
    if not x:
        if len(q):
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, x)
