# S2 최대 힙
import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    x = int(input())
    if not x:
        if len(q):
            print((-1)*(heapq.heappop(q))) # 음수로 넣은 인자를 다시 양수로 바꿈
        else:
            print(0)
    else:
        heapq.heappush(q, -x) # heapq는 최소 힙만 지원해서 음수로 바꿔준 후 heappush