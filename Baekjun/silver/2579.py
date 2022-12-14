# S3 계단 오르기
import sys
input = sys.stdin.readline
N = int(input())
score = [0]
dp = [0]*(N+1)
for _ in range(N):
    score.append(int(input()))
if N==1:
    print(score[1])
else:
    dp[1] = score[1]
    dp[2] = max(score[2], score[2] + score[1])
    for i in range(3, N+1):
        dp[i] = max(dp[i-3]+score[i-1]+score[i], dp[i-2]+score[i])
    print(dp.pop())