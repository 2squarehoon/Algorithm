# S3 피보나치는~
N = int(input())
lst = [0]*51
lst[0] = lst[1] = 1
for n in range(2, 51):
    lst[n] = lst[n-1] + lst[n-2] + 1
print(lst[N]%1000000007)