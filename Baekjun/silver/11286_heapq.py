# S1 절댓값 힙
import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    x = int(input())
    if not x:
        if len(q):
            print(heapq.heappop(q)[1])
        else:
            print(0)
    else:
        heapq.heappush(q, (abs(x), x)) # tuple 형태로 heapq push 가능