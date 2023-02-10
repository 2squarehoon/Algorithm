from collections import deque
def solution(alp, cop, problems):
    max_a, max_c = 0, 0
    for problem in problems:
        max_a = max(problem[0], max_a)
        max_c = max(problem[1], max_c)
    dp = [[99999]*(max_c+1) for _ in range(max_a+1)]
    alp, cop = min(alp, max_a), min(cop, max_c) # 초기값이 목표값을 넘어가버리면 런타임 에러
    dp[alp][cop] = 0 # dp의 의미 : 도달할 수 있는 최단 시간
    for a in range(alp, max_a+1):
        for c in range(cop, max_c+1):
            if a < max_a:
                dp[a+1][c] = min(dp[a+1][c], dp[a][c]+1)
            if c < max_c:
                dp[a][c+1] = min(dp[a][c+1], dp[a][c]+1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    new_a = min(a+alp_rwd, max_a) # 목표값 넘어가면 런타임 에러
                    new_c = min(c+cop_rwd, max_c)
                    dp[new_a][new_c] = min(dp[new_a][new_c], dp[a][c]+cost)
    answer = dp[max_a][max_c]
    return answer