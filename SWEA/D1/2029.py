"""
2029: 몫과 나머지 출력하기
"""

import sys
sys.stdin = open('2029_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    x = numbers[0]
    y = numbers[1]
    print(f'#{test_case} {x // y} {x % y}')