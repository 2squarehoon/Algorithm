N = int(input())
n = 1
while N > n*(n+1)/2:
    n += 1
a = int(N - (n*(n-1)/2))
b = int(n*(n+1)/2 - N + 1)
if n%2:
    print(f'{b}/{a}')
else:
    print(f'{a}/{b}')