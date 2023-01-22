# G5 리모컨
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M:
    broken = list(map(int, input().split()))
else:
    broken = []

min_cnt = abs(100-N) # 현재 채널에서 +, -만 이용한 경우

for nums in range(1000001):
    nums = str(nums)
    for i in range(len(nums)):
        if int(nums[i]) in broken:
            break
        elif i == len(nums)-1:
            min_cnt = min(min_cnt, abs(int(nums)- N) + len(nums))
print(min_cnt)