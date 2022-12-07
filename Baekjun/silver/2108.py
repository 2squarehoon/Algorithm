# S3 통계학
import sys
input = sys.stdin.readline

N = int(input())
lst = []
cnt = [0] * 8001
for _ in range(N):
    num = int(input())
    lst.append(num)
    cnt[num+4000] += 1
lst.sort()
print(round(sum(lst)/N))
print(lst[N//2])
n = 0
most = -4001
count = 0
my_most = 0
for i in range(8001):
    most += 1
    if cnt[i] == max(cnt):
        n += 1
        count += 1
        my_most = most
    if n == 2:
        print(i-4000)
        break
if count == 1:
    print(my_most)
print(max(lst)-min(lst))