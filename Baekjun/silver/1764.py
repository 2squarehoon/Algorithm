# S4 듣보잡
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
D = set()
B = set()
for _ in range(N):
    D.add(str(input().rstrip()))
for _ in range(M):
    B.add(str(input().rstrip()))
ans = sorted(D&B)
print(len(ans))
for name in ans:
    print(name)