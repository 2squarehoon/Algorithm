"""
2068: 최대수 구하기
"""

import sys
sys.stdin = open('2068_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    max_num = 0
    for i in range(len(numbers)-1):
        if numbers[i] > max_num:
            max_num = numbers[i]
    print(f'#{test_case} {max_num}')
