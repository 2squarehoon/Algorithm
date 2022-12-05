# B1 수 정렬하기 3
import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(input().split()[0])
lst.sort()
for number in lst:
    print(number)