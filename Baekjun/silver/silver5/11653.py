N = int(input())
if N == 1:
    print('')
while N != 1:
    for i in range(2, N+1):
        if not N % i:
            N = N // i
            print(i)
            break