"""
2001: 파리 퇴치
"""
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arrays = [list(map(int, input().split())) for _ in range(N)]
    paris = [0] * (N-M+1) * (N-M+1) # 총 부분집합의 개수
    idx = 0
    for i in range(N-M+1): # 파리채의 좌측상단을 기준점으로 가로 좌표, 세로 좌표 수를 구해서 이중for문
        for j in range(N-M+1):
            cnt = 0
            for k in range(M): # 파리채의 좌측상단을 기준으로 잡은 파리 수 카운트
                for l in range(M):
                    cnt += arrays[i+k][j+l]
            paris[idx] = cnt
            idx += 1         
    max_pari = 0
    for x in range(len(paris)):
        if max_pari < paris[x]:
            max_pari = paris[x]
    print(f'#{test_case} {max_pari}')
    
# 처음에 작성한 코드
# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     arrays = []
#     paris = []
#     for array in range(N):
#         arrays.append(list(map(int, input().split())))
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             cnt = 0
#             for k in range(M):
#                 for l in range(M):
#                     cnt += arrays[i+k][j+l]
#             paris.append(cnt)            
#     print(f'#{test_case} {max(paris)}')


