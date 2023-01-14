# S3 2*n 타일링 2
lst = [0]*1001
n = int(input())
lst[1] = 1
lst[2] = 3
for i in range(3, 1001):
    lst[i] = lst[i-1] + lst[i-2]*2
print(lst[n]%10007)