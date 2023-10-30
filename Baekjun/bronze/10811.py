# B2 바구니 뒤집기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [n for n in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    temp = arr[i-1:j]
    temp.reverse()
    arr[i-1:j] = temp
print(*arr)