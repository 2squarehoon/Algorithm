"""
2070: 큰 놈, 작은 놈, 같은 놈
"""

import sys
sys.stdin = open('2070_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    numbers = list(input().split())
    if numbers[0] > numbers[1]:
        print(f'#{test_case} >')
    elif numbers[0] == numbers[1]:
        print(f'#{test_case} =')
    else:
        print(f'#{test_case} <')