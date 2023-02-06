# S2 N과 M (12)
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []
visited = [0]*N
def dfs(start):
    prev = 0
    if len(lst)==M: # 탈출 조건
        print(' '.join(map(str, lst)))
        return
    for i in range(start, N):
        if arr[i] != prev:
            if lst:
                if max(lst) <= arr[i]:
                    lst.append(arr[i])
                    prev = arr[i]
                    dfs(start)
                    lst.pop()
                else:
                    pass
            else:
                lst.append(arr[i])
                prev = arr[i]
                dfs(start)
                lst.pop()
dfs(0)