T = int(input())
for test_case in range(1, T+1):
    H, W, N = map(int, input().split())
    ho = N//H + 1
    if N%H == 0:
        print(H*100 + ho - 1)
    else:
        print((N%H) * 100 + ho)