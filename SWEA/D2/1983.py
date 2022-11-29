"""
1983: 조교의 성적 매기기
"""

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    grades = dict()
    for i in range(1, N+1):
        jungan, gimal, gwaje = map(int, input().split())
        jumsu = jungan * 0.35 + gimal * 0.45 + gwaje * 0.2
        grades[i] = jumsu
    sorted_grade = sorted(grades.items(), key=lambda x: -x[1])
    ranking = 0
    for j in range(1, len(sorted_grade)+1):
        if sorted_grade[j-1][0] == K:
            ranking = j
            break
    if (j*10)/N <= 1:
        print(f'#{test_case} A+')
    elif (j*10)/N <= 2:
        print(f'#{test_case} A0')
    elif (j*10)/N <= 3:
        print(f'#{test_case} A-')
    elif (j*10)/N <= 4:
        print(f'#{test_case} B+')
    elif (j*10)/N <= 5:
        print(f'#{test_case} B0')
    elif (j*10)/N <= 6:
        print(f'#{test_case} B-')
    elif (j*10)/N <= 7:
        print(f'#{test_case} C+')
    elif (j*10)/N <= 8:
        print(f'#{test_case} C0')
    elif (j*10)/N <= 9:
        print(f'#{test_case} C-')
    else:
        print(f'#{test_case} D0')
    

import sys
sys.stdin = open('1983_input.txt')

