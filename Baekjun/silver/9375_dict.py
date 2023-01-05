# S3 패션왕 신해빈

import sys
input = sys.stdin.readline

# dict 활용
T = int(input())
for _ in range(T):
    N = int(input())
    wear = dict()
    for _ in range(N):
        lst = list(map(str, input().split()))
        if lst[1] in wear:
            wear[lst[1]].append(lst[0])
        else:
            wear[lst[1]] = [lst[0]]
    cnt = 1
    for s in wear:
        cnt *= len(wear[s])+1
    print(cnt-1)


# 메모리 초과
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     lst = []
#     subset = [[]]
#     for _ in range(N):
#         a, b = map(str, input().split())
#         lst.append((a, b))
#     for s in lst:
#         size = len(subset)
#         for i in range(size):
#             subset.append(subset[i]+[s])
#     ans = 0
#     for t in subset:
#         cloth = []
#         for j in range(len(t)):
#             cloth.append(t[j][1])
#         x, y = len(cloth), len(set(cloth))
#         if x == y:
#             ans += 1
#     print(ans-1)
