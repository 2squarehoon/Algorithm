import sys
input = sys.stdin.readline

a, b = map(int, input().split())
lst1 = [list(map(int, input().split())) for _ in range(a)]
lst2 = [list(map(int, input().split())) for _ in range(a)]
for i in range(a):
    for j in range(b):
        print((lst1[i][j] + lst2[i][j]), end=' ')
    print()