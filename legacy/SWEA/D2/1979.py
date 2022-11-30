"""
1979: 어디에 단어가 들어갈 수 있을까
"""

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arrays = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    cnt = 0
    for y in range(N): # 가로방향 탐색
        for x in range(N):
            if arrays[y][x] == 1:
                cnt += 1
            if arrays[y][x] == 0 or x == N-1: # 벽에 막힐 때 카운트가 K와 같으면 K길이의 단어를 갖는 것과 같다.
                if cnt == K:
                    answer += 1
                cnt = 0
    for x in range(N): # 세로방향 탐색
        for y in range(N):
            if arrays[y][x] == 1:
                cnt += 1
            if arrays[y][x] == 0 or y == N-1:
                if cnt == K:
                    answer += 1
                cnt = 0
    print(f'#{test_case} {answer}')
                

import sys
sys.stdin = open('1979_input.txt')

