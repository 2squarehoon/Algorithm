"""
1933: 간단한 N의 약수
"""

import sys
sys.stdin = open('1933_input.txt')

N = int(input())
for i in range(N):
    if not N % (i+1):
        print(i+1, end = ' ')