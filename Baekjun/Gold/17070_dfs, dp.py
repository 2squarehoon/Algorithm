# G5 파이프 옮기기 1
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
def dfs(x, y, type): # pypy로 정답, python으로는 시간초과
    global ans
    if y == N-1 and x == N-1:
        ans += 1
        return
    if type == 'h' or type == 'd': # h는 가로, d는 대각, v는 세로
        if x+1<N and not arr[y][x+1]:
            dfs(x+1, y, 'h')
    if type == 'v' or type == 'd':
        if y+1<N and not arr[y+1][x]:
            dfs(x, y+1, 'v')
    if x+1<N and y+1<N and not arr[y+1][x] and not arr[y][x+1] and not arr[y+1][x+1]:
        dfs(x+1, y+1, 'd')

dfs(1, 0, 'h')
print(ans)

