# S5 수 정렬하기 2
import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()
for i in range(N):
    print(lst[i])