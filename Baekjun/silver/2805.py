# S2 나무 자르기
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
start, end = 1, max(lst)
while start <= end:
    mid = (start + end)//2
    cnt = 0
    for wood in lst:
        if mid < wood:
            cnt += wood-mid
    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)