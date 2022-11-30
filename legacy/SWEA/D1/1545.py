"""
1545: 거꾸로 출력해 보아요
"""

import sys
sys.stdin = open('1545_input.txt')

n = int(input())
for i in range(n+1):
    print(n-i, end = ' ')
