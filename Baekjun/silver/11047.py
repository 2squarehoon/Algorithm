# S4 동전 0
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.insert(0, int(input()))
ans = 0
for coin in lst:
    ans += K//coin
    K = K%coin
print(ans)