# S3 파도반 수열
import sys
input = sys.stdin.readline
lst = [1]*100
lst[3] = 2
lst[4] = 2
T = int(input())
for i in range(5, 100):
    lst[i] = lst[i-1] + lst[i-5]
for _ in range(T):
    print(lst[int(input())-1])