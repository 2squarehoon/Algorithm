from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solution(maps):
    N = len(maps[0])  # 가로
    M = len(maps)  # 세로
    visited = [[0] * N for _ in range(M)]
    answer = []
    for y in range(M):
        for x in range(N):
            if maps[y][x] == 'X' or visited[y][x]:
                continue
            q = deque()
            q.append((x, y))
            visited[y][x] = 1
            temp = 0
            while q:
                ax, ay = q.popleft()  # x, y로 했다가 왜그런지는 모르겠는데 에러남
                temp += int(maps[ay][ax])
                for d in range(4):
                    nx, ny = ax + dx[d], ay + dy[d]
                    if 0 <= nx < N and 0 <= ny < M and maps[ny][nx] != 'X' and not visited[ny][nx]:
                        q.append((nx, ny))
                        visited[ny][nx] = 1
            if temp:
                answer.append(temp)
    return sorted(answer) if answer else [-1]