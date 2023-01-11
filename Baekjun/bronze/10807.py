# B5 개수 세기 (급하게 하나 풀어야해서...)
N = int(input())
lst = list(map(int, input().split()))
v = int(input())
ans = 0
for n in lst:
    if n == v:
        ans += 1
print(ans)