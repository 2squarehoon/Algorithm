N = int(input())
arr = []
for n in range(N, 0, -1):
    lst = [N, n]
    i = 0
    while True:
        if lst[i]-lst[i+1] < 0:
            break
        lst.append(lst[i]-lst[i+1])
        i += 1
    arr.append(lst)
max_cnt = 0
max_idx = 0
for j in range(len(arr)):
    if len(arr[j]) > max_cnt:
        max_cnt = len(arr[j])
        max_idx = j
print(max_cnt)
print(*arr[max_idx])