def bingo(lst):
    cnt = 0
    for i in range(5):
        if lst[i][0] == lst[i][1] == lst[i][2] == lst[i][3] == lst[i][4] == 1:
            cnt += 1
        if lst[0][i] == lst[1][i] == lst[2][i] == lst[3][i] == lst[4][i] == 1:
            cnt += 1
    if lst[0][0] == lst[1][1] == lst[2][2] == lst[3][3] == lst[4][4] == 1:
        cnt += 1
    if lst[4][0] == lst[3][1] == lst[2][2] == lst[1][3] == lst[0][4] == 1:
        cnt += 1
    return cnt

chulsu = [list(map(int, input().split())) for _ in range(5)]
arr = [[0]*5 for _ in range(5)]
mc = []
for _ in range(5):
    mc.extend(list(map(int, input().split())))
ans = 0
for n in range(25):
    for i in range(5):
        for j in range(5):
            if mc[n] == chulsu[j][i]:
                arr[j][i] = 1
    ans += 1
    if bingo(arr) == 3:
        print(ans)
        break


