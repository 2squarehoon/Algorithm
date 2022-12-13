# S5 팩토리얼 0의 개수
N = int(input())
ans = 0
for i in range(1, N+1):
    if not i%5:
        ans += 1
    if not i%25:
        ans += 1
    if not i%125:
        ans += 1
print(ans)