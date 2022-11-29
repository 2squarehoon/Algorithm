di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for _ in range(10):
    tc = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    ans = 0
    for x in range(1, 101):
        position = [[0] * 100 for _ in range(100)]
        ni = -1
        nj = x
        k = 0
        if arr[0][x] == 1:
            while True:
                ni += di[k]
                nj += dj[k]
                position[ni][nj] = 1
                if (k == 1 or k == 3) and arr[ni+1][nj] == 1:
                    k = 0
                if k == 0 and arr[ni][nj+1] == 1:
                    k = 1
                if k == 0 and arr[ni][nj-1] == 1:
                    k = 3
                if ni == 99:
                    if arr[ni][nj] == 2:
                        ans = x
                        break
                    else:
                        break
    print(f'#{tc} {ans-1}')


