N = int(input())
x = False
for m in range(1, N+1):
    bhh = m
    cnt = m
    while m != 0:
        bhh += m % 10
        m = m//10
    if bhh == N:
        print(cnt)
        x = True
        break
if not x:
    print(0)