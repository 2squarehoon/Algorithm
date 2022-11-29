"""
1859: 백만장자 프로젝트
"""

T = int(input())
for test_case in range(1, T+1):
    cnt = 0
    N = int(input())
    numbers = list(map(int, input().split()))
    max_num = numbers[-1]
    for i in range(len(numbers)-1, -1, -1):
        if numbers[i] >= max_num:
            max_num = numbers[i]
        else:
            cnt += (max_num - numbers[i])
    print(f'#{test_case} {cnt}')


import sys
sys.stdin = open('1859_input.txt')

