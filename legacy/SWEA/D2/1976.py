"""
1976: 시각 덧셈
"""

T = int(input())
for test_case in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h, m = (0, 0)
    if m1 + m2 >= 60:
        m = m1 + m2 - 60
        h = h1 + h2 + 1
    else:
        m = m1 + m2
        h = h1 + h2
    if h > 12:
        h = h - 12
    print(f'#{test_case} {h} {m}')

import sys
sys.stdin = open('1976_input.txt')

