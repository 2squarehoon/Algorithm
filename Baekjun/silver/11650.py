# S5 좌표 정렬하기
import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

# for i in range(N-1, 0, -1):
#     for j in range(i):
#         if lst[j][0] > lst[j+1][0]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
# for i in range(N-1, 0, -1):
#     for j in range(i):
#         if lst[j][0] == lst[j+1][0] and lst[j][1] > lst[j+1][1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
# 버블정렬 시간초과

# for i in range(N-1):
#     min_idx = i
#     for j in range(i+1, N):
#         if lst[min_idx][0] > lst[j][0]:
#             min_idx = j
#     lst[i], lst[min_idx] = lst[min_idx], lst[i]
#
# for i in range(N-1):
#     min_idx = i
#     for j in range(i+1, N):
#         if lst[min_idx][0] == lst[j][0] and lst[min_idx][1] > lst[j][1]:
#             min_idx = j
#     lst[i], lst[min_idx] = lst[min_idx], lst[i]
# 선택정렬 시간초과
lst.sort()
# 내장함수 짱짱맨이네

for numbers in lst:
    print(*numbers)