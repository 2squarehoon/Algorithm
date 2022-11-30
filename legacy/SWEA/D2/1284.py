"""
1284: 수도 요금 경쟁
"""

T = int(input())
for test_case in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    A = W * P
    if R > W:
        B = Q
    else:
        B = Q + (W-R)*S
    print(f'#{test_case} {min(A, B)}')
