N = int(input())
def baedal(N):
    cnt = 0
    while N % 5:
        cnt += 1
        N = N-3
        if N <= 2 and N != 0:
            return -1
            break
    return cnt + N//5
print(baedal(N))