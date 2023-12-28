# S5 다리 놓기

def factorial(n):
    cnt = 1
    for i in range(1, n+1):
        cnt *= i
    return cnt

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    m, n = max(N, M), min(N, M)
    print(factorial(m)//(factorial(n)*factorial(m-n)))