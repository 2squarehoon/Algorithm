"""
2007: 패턴 마디의 길이
"""
T = int(input())
for test_case in range(1, T+1):
    str1 = str(input())
    for i in range(2, 11):
        if str1[0:i] == str1[i:2*i]:
            print(f'#{test_case} {i}')
            break
            

import sys
sys.stdin = open('2007_input.txt')

