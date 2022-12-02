# S4 수 찾기
import sys
N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
for b in B:
    if b in A:
        print(1)
    else:
        print(0)
