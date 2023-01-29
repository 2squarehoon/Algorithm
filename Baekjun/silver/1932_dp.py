# S1 정수 삼각형
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(i+1):
        if j == 0: # 왼쪽으로 쭉 내려옴
            arr[i][0] += arr[i-1][0]
        elif j == i: # 오른쪽으로 쭉 내려옴
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
print(max(arr[n-1]))