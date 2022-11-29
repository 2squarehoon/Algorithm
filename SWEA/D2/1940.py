"""
1940: 가랏! RC카!
"""

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    v = 0
    d = 0
    for i in range(N):
        try:
            a, b = map(int, input().split())
        except ValueError:
            a = 0
        if a == 0:
            d += v
        elif a == 1:
            v += b
            d += v
        else:
            v -= b
            if v < 0:
                v = 0
            d += v
    print(f'#{test_case} {d}')  

    