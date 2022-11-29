"""
1970: 쉬운 거스름돈
"""

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    currency = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = []
    for x in currency:
        cnt.append(N//x)
        N = N%x
    print(f'#{test_case}')
    print(*cnt)