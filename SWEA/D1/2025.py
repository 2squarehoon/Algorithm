"""
2025: N줄덧셈
"""

import sys
sys.stdin = open('2025_input.txt')

number = int(input())
sum1 = 0
for i in range(number+1):
    sum1 += i
print(sum1)