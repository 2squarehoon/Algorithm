"""
2063: 중간값 찾기
"""

import sys
sys.stdin = open('2063_input.txt')

T = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)
print(numbers[T//2])

