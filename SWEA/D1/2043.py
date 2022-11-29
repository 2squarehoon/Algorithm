"""
2043: 서랍의 비밀번호
"""

import sys
sys.stdin = open('2043_input.txt')

numbers = list(map(int, input().split()))
P = numbers[0]
K = numbers[1]
print(abs(P-K) + 1)