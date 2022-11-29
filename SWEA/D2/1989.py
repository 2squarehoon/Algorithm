"""
1989: 초심자의 회문검사
"""
T = int(input())
for test_case in range(1, T+1):
    word = str(input().rstrip())
    n = len(word)//2
    for i in range(n):
        if word[i] != word[len(word)-i-1]:
            m = 0
            break
        else:
            m = 1
    print(f'#{test_case} {m}')


import sys
sys.stdin = open('1989_input.txt')

