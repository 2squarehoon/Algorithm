"""
1986: 지그재그 숫자
"""
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if i % 2:
            cnt += i
        else:
            cnt -= i
    print(f'#{test_case} {cnt}')

import sys
sys.stdin = open('1986_input.txt')

