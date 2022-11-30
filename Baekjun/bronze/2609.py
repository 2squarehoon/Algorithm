# B1 최대공약수와 최소공배수

n, m = map(int, input().split())
smallNum, bigNum = min(n, m), max(n, m)
GCD = 1
for i in range(1, smallNum+1):
    if n % i == 0 and m % i == 0:
        GCD = i
print(GCD)
print(n*m//GCD)