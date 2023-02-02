# S2 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline

N = int(input())
Ai = list(map(int, input().split()))
dp = [0]*N
for i in range(N):
    for j in range(i):
        if Ai[i]>Ai[j] and dp[i]<dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))