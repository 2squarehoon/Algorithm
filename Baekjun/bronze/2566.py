lst = [list(map(int, input().split())) for _ in range(9)]
n = 0
loca = (0, 0)
for i in range(9):
    for j in range(9):
        if lst[i][j] >= n:
            n = lst[i][j]
            loca = (i+1, j+1)
print(n)
print(*loca)