"""
1959: 두 개의 숫자열
"""

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    lst = []
    if M > N:
        for x in range(M-N+1):
            cnt = 0
            for idx in range(len(Ai)):
                cnt += Ai[idx]*Bj[idx+x]
            lst.append(cnt)
    else:
        for x in range(N-M+1):
            cnt = 0
            for idx in range(len(Bj)):
                cnt += Ai[idx+x]*Bj[idx]
            lst.append(cnt)
    print(f'#{test_case} {max(lst)}')
