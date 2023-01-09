# S3 2*n 타일링

n = int(input())
lst = [0]*1001
lst[0] = 1
lst[1] = 2
if n >= 3:
    for n in range(2, n+1):
        lst[n] = lst[n-1] + lst[n-2]
print(lst[n-1]%10007)