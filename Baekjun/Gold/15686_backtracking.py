# G5 치킨 배달
import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
house, chicken = [], []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j]==1:
            house.append((i, j))
        elif row[j]==2:
            chicken.append((i, j))
ans = 99999999999999
for c in combinations(chicken, M): # M개의 치킨집 선택
    temp = 0
    for h in house:
        c_len = 99999999
        for j in range(M):
            c_len = min(c_len, abs(h[0]-c[j][0]) + abs(h[1]-c[j][1]))
        temp += c_len
    ans = min(ans, temp)
print(ans)