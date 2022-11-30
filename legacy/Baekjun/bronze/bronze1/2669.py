lst = [[0]*100 for _ in range(100)]
for n in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1-1, x2-1):
        for y in range(y1-1, y2-1):
            lst[y][x] = 1
ans = 0
for i in range(100):
    for j in range(100):
        ans += lst[j][i]
print(ans)