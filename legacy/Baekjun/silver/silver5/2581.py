M = int(input())
N = int(input())
lst = [0] * (N-M+1)
for i in range(M, N+1):
    cnt = 0
    for j in range(1, i+1):
        if not i % j:
            cnt += 1
    if cnt == 2:
        lst[M-i] = i
sum_num = 0
min_num = 10001
for idx in range(N-M+1):
    if lst[idx] == 0:
        continue
    sum_num += lst[idx]
    if min_num > lst[idx]:
        min_num = lst[idx]
if sum_num == 0:
    print(-1)
else:
    print(sum_num)
    print(min_num)
