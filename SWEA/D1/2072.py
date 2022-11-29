"""
2072: 홀수만 구하기
"""

import sys
sys.stdin = open("C:/Users/SH/Desktop/new TIL/SWEA/2072_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    numbers = map(int, input().split())
    result = 0
    for number in numbers:
        if number % 2:
            result += number
    print(f'#{test_case} {result}')