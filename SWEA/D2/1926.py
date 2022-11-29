"""
1926: 간단한 369게임
"""

N = int(input())
for i in range(1, N+1):
    clap = str(i).count('3') + str(i).count('6') + str(i).count('9')
    if clap == 0:
        print(i, end = ' ')
    else:
        print('-'*clap, end = ' ')


import sys
sys.stdin = open('1926_input.txt')

