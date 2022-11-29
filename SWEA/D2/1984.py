"""
1984: 중간 평균값 구하기
"""

T = int(input())
for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))
    max_num = max(numbers)
    min_num = min(numbers)
    # numbers = numbers.remove(max_num)
    # numbers = numbers.remove(min_num)
    # print(f'#{test_case} {sum(numbers)/len(numbers)}')
    print(f'#{test_case} {(sum(numbers)- max_num - min_num) / (len(numbers) - 2):.0f}')

import sys
sys.stdin = open('1984_input.txt')

