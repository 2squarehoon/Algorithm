# S2 베르트랑 공준

import sys
from math import sqrt
input = sys.stdin.readline
# pypy로 돌려야 풀림, python으로는 시간초과
while True:
    n = int(input())
    if not n:
        break
    cnt = 0
    for i in range(n+1, n*2+1):
        if i == 2:
            cnt += 1
            continue
        else:
            for j in range(2, int(1+sqrt(i))):
                if not i%j:
                    break
            else:
                cnt += 1
    print(cnt)

# 소수 리스트 따로 만들기
def prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if not n%i:
            return False
    return True

lst = []
for j in range(2, 246913):
    if prime(j):
        lst.append(j)
while True:
    n = int(input())
    if not n:
        break
    cnt = 0
    for pnum in lst:
        if n < pnum <= n*2:
            cnt += 1
    print(cnt)