"""
2071: 평균값 구하기
"""

import sys
sys.stdin = open('2071_input.txt','r')

T = int(input())
for test_case in range(1, T + 1):
    numbers = map(int, input().split())
    result = 0
    for number in numbers:
        result += number
    avg = round(result / 10)
    print(f'#{test_case} {avg}')

