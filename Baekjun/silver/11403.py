# S1 경로 찾기 (플로이드-워셜 알고리즘)
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            if arr[j][k] == 1 or (arr[j][i]==1 and arr[i][k]==1):
                arr[j][k]=1
for y in arr:
    for x in y:
        print(x, end=' ')
    print()