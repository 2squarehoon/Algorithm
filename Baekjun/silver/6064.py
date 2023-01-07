# S1 카잉 달력
import sys
import math

# 시간초과
# T = int(input())
# for _ in range(T):
#     M, N, x, y = map(int, input().split())
#     a, b = 1, 1
#     ans = 1
#     while True:
#         if (a, b) == (x, y) or (a, b) == (M, N):
#             break
#         a += 1
#         b += 1
#         ans += 1
#         if a > M:
#             a = 1
#         if b > N:
#             b = 1
#     if ans == math.lcm(M,N) and (x, y) != (M, N):
#         print(-1)
#     else:
#         print(ans)

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    flag = 1
    while x <= M*N:
        if x%N == y%N:
            print(x)
            flag = 0
            break
        x += M
    if flag:
        print(-1)