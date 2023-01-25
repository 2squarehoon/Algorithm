# S1 IOIOI
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = list(input().rstrip())
# 시간초과코드
# Pn = 'I'+'OI'*N
# cnt = 0
# for i in range(M-2*N):
#     word = ''
#     for j in range(i, i+2*N+1):
#         word += S[j]
#     if word == Pn:
#         cnt += 1
# print(cnt)

ans, cnt, i = 0, 0, 1
while i < (M-1):
    if S[i-1]+S[i]+S[i+1] == 'IOI':
        i += 2
        cnt += 1
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0
print(ans)