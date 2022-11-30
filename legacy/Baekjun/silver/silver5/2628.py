x, y = map(int, input().split())
N = int(input())
garo = [0, x]
sero = [0, y]
for _ in range(N):
    idx, n = map(int, input().split())
    if idx == 0:
        sero.append(n)
    else:
        garo.append(n)
garo.sort()
sero.sort()
max_num = 0
for i in range(len(garo)-1):
    for j in range(len(sero)-1):
        if max_num < (garo[i+1]-garo[i]) * (sero[j+1]-sero[j]):
            max_num = (garo[i+1]-garo[i]) * (sero[j+1]-sero[j])
print(max_num)
