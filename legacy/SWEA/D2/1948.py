"""
1948: 날짜 계산기
"""

T = int(input())
for test_case in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = d2-d1+1
    for i in range(m2-m1):
        days += months[m1-1+i]
    print(f'#{test_case} {days}')