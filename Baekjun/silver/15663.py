# S2 N과 M (9)
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []
visited = [0]*N
def dfs():
    prev = 0
    if len(lst)==M: # 탈출 조건
        print(' '.join(map(str, lst)))
        return
    for i in range(N):
        if arr[i] != prev and not visited[i]:
            lst.append(arr[i])
            prev = arr[i]
            visited[i] = 1
            dfs()
            lst.pop()
            visited[i] = 0
dfs()