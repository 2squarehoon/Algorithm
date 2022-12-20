# S5 집합
import sys
input = sys.stdin.readline
S = set()
M = int(input())
for _ in range(M):
    order = input().split()
    if len(order) == 1:
        if order[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()

    else:
        func, x = order[0], int(order[1])
        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)
