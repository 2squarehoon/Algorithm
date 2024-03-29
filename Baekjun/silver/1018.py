# S4 체스판 다시 칠하기

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
result = []
for i in range(N-7):
    for j in range(M-7):
        draw1 = 0
        draw2 = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if arr[a][b] != 'B':
                        draw1 += 1
                    if arr[a][b] != 'W':
                        draw2 += 1
                else:
                    if arr[a][b] != 'W':
                        draw1 += 1
                    if arr[a][b] != 'B':
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)

print(min(result))