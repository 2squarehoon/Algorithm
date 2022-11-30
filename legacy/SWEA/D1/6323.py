"""
6323: 8. 함수의 기초 4
"""
def fibonaci(n):
    if T == 1:
        return [1]
    elif T == 2:
        return [1, 1]
    fibo = [1, 1]
    for i in range(2, T):
        fibo.append(fibo[i-2] + fibo[i-1])
    return fibo

T = int(input())
print(fibonaci(T))