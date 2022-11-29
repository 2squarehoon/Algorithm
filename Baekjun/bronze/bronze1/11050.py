N, K = map(int, input().split())
if K < 0 or K > N:
    print(0)
else:
    cnt = 1
    for i in range(1, N+1):
        cnt *= i
    for j in range(1, K+1):
        cnt /= j
    for k in range(1, N-K+1):
        cnt /= k
    print(int(cnt))