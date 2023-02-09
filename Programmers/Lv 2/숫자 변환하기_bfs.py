from collections import deque
def solution(x, y, n):
    visited = [0]*1000001
    visited[x] = 1
    q = deque()
    q.append(x)
    while q:
        i = q.popleft()
        for ni in [i*2, i*3, i+n]:
            if ni<=y and not visited[ni]:
                q.append(ni)
                visited[ni] = visited[i]+1
    answer = visited[y] -1
    return answer