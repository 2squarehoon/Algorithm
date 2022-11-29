"""
1938: 아주 간단한 계산기
"""

import sys
sys.stdin = open('1938_input.txt')

numbers = list(map(int, input().split()))
a = numbers[0]
b = numbers[1]
print(a+b)
print(a-b)
print(a*b)
print(a//b)
