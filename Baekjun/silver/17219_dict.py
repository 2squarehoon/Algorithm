# S4 비밀번호 찾기
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
site = dict()
for _ in range(N):
    a, b = map(str, input().split())
    site[a] = b
for _ in range(M):
    print(site[input().rstrip()])