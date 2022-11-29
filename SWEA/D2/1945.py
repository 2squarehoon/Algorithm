"""
1945: 간단한 소인수분해
"""

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    soinsu = [0]*5
    while not N%2:
        N /= 2
        soinsu[0] += 1
    while not N%3:
        N /= 3
        soinsu[1] += 1
    while not N%5:
        N /= 5
        soinsu[2] += 1
    while not N%7:
        N /= 7
        soinsu[3] += 1
    while not N%11:
        N /= 11
        soinsu[4] += 1
    print(f'#{test_case}', end= ' ')
    print(*soinsu)