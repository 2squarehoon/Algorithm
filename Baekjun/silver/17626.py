# S3 Four Squares
N = int(input())
dp = [0]*(N+1)
k = 1
while k**2 <= N:
    dp[k**2] = 1
    k += 1
for i in range(1, N+1):
    if dp[i] != 0:
        continue
    j = 1
    while j**2 <= i:
        if dp[i] == 0:
            dp[i] = dp[j**2] + dp[i-j**2]
        else:
            dp[i] = min(dp[i], dp[j**2]+dp[i-j**2])
        j += 1
print(dp[N])