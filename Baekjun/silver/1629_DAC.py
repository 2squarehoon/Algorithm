# S1 곱셈
A, B, C = map(int, input().split())
def multi(a, b, c):
    if b==1:
        return a%c
    elif not b%2:
        return (multi(a, b//2, c)**2)%c
    else:
        return((multi(a, b//2, c)**2)*a)%c
print(multi(A, B, C))