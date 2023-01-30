# S3 조합
n, m = map(int, input().split())

def factorial(x):
    num = 1
    for i in range(x):
        num *= i+1
    return num
print(factorial(n)//(factorial(n-m)*factorial(m)))