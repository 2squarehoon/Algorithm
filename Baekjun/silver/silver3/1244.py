def switch(arr, idx):
    if arr[idx] == 1:
        arr[idx] = 0
    else:
        arr[idx] = 1
    return arr

N = int(input())
swt = list(map(int, input().split()))
stu = int(input())
for i in range(stu):
    s, n = map(int, input().split())
    if s == 1:
        for j in range(n-1, N, n):
            switch(swt, j)
    else:
        switch(swt, n-1)
        for k in range(N//2):
            if n + k > N or n - k < 1:
                break
            if swt[n+k-1] == swt[n-k-1]:
                switch(swt, n+k-1)
                switch(swt, n-k-1)
            else:
                break
cnt = 0
for n in swt:
    print(n, end=' ')
    cnt += 1
    if not cnt%20:
        print('')