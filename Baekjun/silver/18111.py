# S2 마인크래프트
# pypy로 제출, python으로는 시간초과
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tall = 0
ans_time = 9999999999999999999999
for floor in range(257):
    take_block, use_block = 0, 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > floor:
                take_block += arr[i][j] - floor
            else:
                use_block += floor - arr[i][j]
    inventory = B + take_block
    if inventory < use_block:
        continue
    time = take_block * 2 + use_block
    if time <= ans_time:
        ans_time = time
        tall = floor
print(ans_time, tall)
