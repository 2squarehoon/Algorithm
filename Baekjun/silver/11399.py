# S4 ATM

import sys
input = sys.stdin.readline

N = int(input())
lst = sorted(list(map(int, input().split())))
cnt, ans = 0, 0
for n in lst:
    cnt += n
    ans += cnt
print(ans)