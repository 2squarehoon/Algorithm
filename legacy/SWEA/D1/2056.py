"""
2056: 연월일 달력
"""

import sys
sys.stdin = open('2056_input.txt')

T = int(input())
for test_case in range(1, T+1):
    date = str(input())
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    # print(date, month, day, type(month))
    if int(month) > 12 or int(month) == 0:
        print(f'#{test_case} -1')
    elif int(month) == 2 and int(day) > 28:
        print(f'#{test_case} -1')
    elif int(month) % 2 and int(day) > 31 or int(day) == 0:
        print(f'#{test_case} -1')
    elif int(day) > 30 or int(day) == 0:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {year}/{month}/{day}')