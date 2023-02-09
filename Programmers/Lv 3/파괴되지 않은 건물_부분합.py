def solution(board, skill):
    N, M = len(board[0]), len(board)
    sum_lst = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
    for t, r1, c1, r2, c2, degree in skill:
        if t == 2:
            degree *= -1
        sum_lst[r1][c1] -= degree
        sum_lst[r1][c2 + 1] += degree
        sum_lst[r2 + 1][c1] += degree
        sum_lst[r2 + 1][c2 + 1] -= degree

    for y in range(M):
        for x in range(N):
            sum_lst[y][x + 1] += sum_lst[y][x]
    for x in range(N):
        for y in range(M):
            sum_lst[y + 1][x] += sum_lst[y][x]
    answer = 0
    for y in range(M):
        for x in range(N):
            if board[y][x] + sum_lst[y][x] > 0:
                answer += 1
    return answer