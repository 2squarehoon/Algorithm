# S4 문자열 집합

N, M = map(int, input().split())
S = set()
for _ in range(N):
    S.add(input())
ans = 0
for _ in range(M):
    word = input()
    if word in S:
        ans += 1
print(ans)