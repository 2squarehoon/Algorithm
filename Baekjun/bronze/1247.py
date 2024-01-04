# B3 부호
from sys import stdin
for _ in range(3):
    n = int(stdin.readline())
    cnt = 0
    for _ in range(n):
        cnt += int(stdin.readline())
    if cnt>0:
        print("+")
    elif cnt==0:
        print(0)
    else:
        print("-")