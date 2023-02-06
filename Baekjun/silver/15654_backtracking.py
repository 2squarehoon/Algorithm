# S3 N과 M (5)
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []
def dfs(start):
    if len(lst)==M: # 탈출 조건
        print(' '.join(map(str, lst)))
        return
    for i in range(N):
        if arr[i] in lst: # 중복 제거
            continue
        lst.append(arr[i])
        dfs(start+1)
        lst.pop()
dfs(0)