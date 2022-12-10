# S2 랜선 자르기
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lst = []
for _ in range(K):
    lst.append(int(input()))
start, end = 1, max(lst)

while start <= end:
    mid = (start + end)//2
    cnt = 0
    for line in lst:
        cnt += line//mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)