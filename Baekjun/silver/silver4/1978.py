N = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in range(N):
    cnt = 0
    for j in range(1, arr[i]+1):
        if not arr[i] % j:
            cnt += 1
    if cnt == 2:
        ans += 1
print(ans)