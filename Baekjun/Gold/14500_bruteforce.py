# G4 테트로미노
import sys
input = sys.stdin.readline

def check(n):
    global ans
    if n > ans:
        ans = n

def ㅡ(a, b):
    for i in range(a, a+4):
        cnt = arr[i][b] + arr[i][b+1] + arr[i][b+2] + arr[i][b+3]
        check(cnt)
    for j in range(b, b+4):
        cnt = arr[a][j] + arr[a+1][j] + arr[a+2][j] + arr[a+3][j]
        check(cnt)

def ㅁ(a, b):
    for i in range(a, a+3):
        for j in range(b, b+3):
            cnt = arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1]
            check(cnt)

def ㄱ(a, b):
    for i in range(a, a+2):
        for j in range(b, b+3):
            cnt = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j+1]
            check(cnt)
    for i in range(a, a+2):
        for j in range(b+1, b+4):
            cnt = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j-1]
            check(cnt)
    for i in range(a, a+3):
        for j in range(b, b+2):
            cnt = arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i][j+2]
            check(cnt)
    for i in range(a, a+3):
        for j in range(b, b+2):
            cnt = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+2]
            check(cnt)
    for i in range(a, a+2):
        for j in range(b, b+3):
            cnt = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+2][j]
            check(cnt)
    for i in range(a, a+2):
        for j in range(b, b+3):
            cnt = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1]
            check(cnt)
    for i in range(a, a+3):
        for j in range(b, b+2):
            cnt = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2]
            check(cnt)
    for i in range(a+1, a+4):
        for j in range(b, b+2):
            cnt = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i-1][j+2]
            check(cnt)

def Z(a, b):
    for i in range(a, a+2):
        for j in range(b, b+3):
            cnt = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1]
            check(cnt)
    for i in range(a+1, a+4):
        for j in range(b, b+2):
            cnt = arr[i][j] + arr[i][j+1] + arr[i-1][j+1] + arr[i-1][j+2]
            check(cnt)
    for i in range(a, a+3):
        for j in range(b, b+2):
            cnt = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j+2]
            check(cnt)
    for i in range(a+2, a+4):
        for j in range(b, b+3):
            cnt = arr[i][j] + arr[i-1][j] + arr[i-1][j+1] + arr[i-2][j+1]
            check(cnt)
def ㅗ(a, b):
    for i in range(a+1, a+3):
        for j in range(b, b+3):
            cnt = arr[i][j] + arr[i-1][j] + arr[i+1][j] + arr[i][j+1]
            check(cnt)
    for i in range(a, a+3):
        for j in range(b+1, b+3):
            cnt = arr[i][j] + arr[i][j-1] + arr[i][j+1] + arr[i+1][j]
            check(cnt)
    for i in range(a+1, a+4):
        for j in range(b+1, b+3):
            cnt = arr[i][j] + arr[i][j-1] + arr[i][j+1] + arr[i-1][j]
            check(cnt)
    for i in range(a+1, a+3):
        for j in range(b+1, b+4):
            cnt = arr[i][j] + arr[i-1][j] + arr[i+1][j] + arr[i][j-1]
            check(cnt)

def tetro(a, b):
    ㅡ(a, b)
    ㅁ(a, b)
    ㄱ(a, b)
    Z(a, b)
    ㅗ(a, b)

N ,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N-3):
    for j in range(M-3):
        tetro(i, j)
print(ans)