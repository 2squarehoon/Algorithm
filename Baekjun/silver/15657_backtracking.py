# S3 N과 M (8)
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []
def dfs(start):
    if len(lst)==M: # 탈출 조건
        print(' '.join(map(str, lst)))
        return
    for i in range(start-1, N):
        lst.append(arr[i])
        dfs(i+1)
        lst.pop()
dfs(1)