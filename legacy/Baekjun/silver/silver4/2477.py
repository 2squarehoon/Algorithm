K = int(input())
arr = [[0, 0] for _ in range(4)]
for n in range(6):
    t, N = map(int, input().split())
    if arr[t-1][0] == 0:
        arr[t-1][0] = N
    else:
        arr[t-1][1] = N
    