# S3 1, 2, 3 더하기
import sys
input = sys.stdin.readline
T = int(input())
lst = [0]*10
lst[0] = 1
lst[1] = 2
lst[2] = 4
for i in range(3, 10):
    lst[i] = lst[i-1] + lst[i-2] + lst[i-3]
for _ in range(T):
    print(lst[int(input())-1])