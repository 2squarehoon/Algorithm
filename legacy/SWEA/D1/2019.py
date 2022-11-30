"""
2019: 더블더블
"""

import sys
sys.stdin = open('2019_input.txt')

n = int(input())
for i in range(n+1):
    print (1 * (2 ** i), end = ' ')