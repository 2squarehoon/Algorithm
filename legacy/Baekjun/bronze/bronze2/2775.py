T = int(input())
for test_case in range(1, T+1):
    k = int(input())
    n = int(input())
    arr = [x for x in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            arr[j] += arr[j-1]
    print(arr[-1])
    
# 순열 (n+i)C(i+1)