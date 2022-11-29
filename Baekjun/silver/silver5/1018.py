N, M = map(int, input().split())
board = [str(input()) for _ in range(N)]
min_cnt = 25000
k = 0
for i in range(N-7):
    for j in range(M-7):
        for n in range(4):
            if n == 0:
                cnt = 0
                arr = [['']*M for _ in range(N)]
                for k in range(8):
                    for l in range(8):
                        arr[i+k][j+l] = board[i+k][j+l]
                if arr[i][j] == 'W':
                    for y in range(8):
                        for x in range(8):
                            if (x+y) % 2 and arr[i+y][j+x] == 'W':
                                cnt += 1
                            elif (x+y) % 2 == 0 and arr[i+y][j+x] == 'B':
                                cnt += 1
                else:
                    for y in range(8):
                        for x in range(8):
                            if (x+y) % 2 and arr[i+y][j+x] == 'B':
                                cnt += 1
                            elif (x+y) % 2 == 0 and arr[i+y][j+x] == 'W':
                                cnt += 1
                if min_cnt > cnt:
                    min_cnt = cnt
            elif n == 1: 
                cnt = 0
                arr = [['']*M for _ in range(N)]
                for k in range(8):
                    for l in range(8):
                        arr[-i-k-1][-j-l-1] = board[-i-k-1][-j-l-1]
                if arr[-i-1][-j-1] == 'W':
                    for y in range(8):
                        for x in range(8):
                            if (x+y) % 2 and arr[-i-y-1][-j-x-1] == 'W':
                                cnt += 1
                            elif (x+y) % 2 == 0 and arr[-i-y-1][-j-x-1] == 'B':
                                cnt += 1
                else:
                    for y in range(8):
                        for x in range(8):
                            if (x+y) % 2 and arr[-i-y-1][-j-x-1] == 'B':
                                cnt += 1
                            elif (x+y) % 2 == 0 and arr[-i-y-1][-j-x-1] == 'W':
                                cnt += 1
                if min_cnt > cnt:
                    min_cnt = cnt
            elif n == 2:
                cnt = 0
                arr = [['']*M for _ in range(N)]
                for k in range(8):
                    for l in range(8):
                        arr[i+k][-j-l-1] = board[i+k][-j-l-1]
                if arr[i][-j-1] == 'W':
                    for y in range(8):
                        for x in range(8):
                            if (x+y) % 2 and arr[i+y][-j-x-1] == 'W':
                                cnt += 1
                            elif (x+y) % 2 == 0 and arr[i+y][-j-x-1] == 'B':
                                cnt += 1
                else:
                    for y in range(8):
                        for x in range(8):
                            if (x+y) % 2 and arr[i+y][-j-x-1] == 'B':
                                cnt += 1
                            elif (x+y) % 2 == 0 and arr[i+y][-j-x-1] == 'W':
                                cnt += 1
                if min_cnt > cnt:
                    min_cnt = cnt
            else:
                cnt = 0
                arr = [['']*M for _ in range(N)]
                for k in range(8):
                    for l in range(8):
                        arr[-i-k-1][j+l] = board[-i-k-1][j+l]
                if arr[-i-1][j] == 'W':
                    for y in range(8):
                        for x in range(8):
                            if (x+y) % 2 and arr[-i-y-1][j+x] == 'W':
                                cnt += 1
                            elif (x+y) % 2 == 0 and arr[-i-y-1][j+x] == 'B':
                                cnt += 1
                else:
                    for y in range(8):
                        for x in range(8):
                            if (x+y) % 2 and arr[-i-y-1][j+x] == 'B':
                                cnt += 1
                            elif (x+y) % 2 == 0 and arr[-i-y-1][j+x] == 'W':
                                cnt += 1
                if min_cnt > cnt:
                    min_cnt = cnt
print(min_cnt)
