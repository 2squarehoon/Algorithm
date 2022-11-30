"""
1936: 1대1 가위바위보
"""

import sys
sys.stdin = open('1936_input.txt')

numbers = list(map(int, input().split()))
A = numbers[0]
B = numbers[1]
if B-A == 1 or B-A == -2:
    print('B')
else:
    print('A')
