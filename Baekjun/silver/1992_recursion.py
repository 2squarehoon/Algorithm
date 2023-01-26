# S1 쿼드트리
import sys
input = sys.stdin.readline
N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
def check(a, b, n):
    flag = 0 # 초기값 0, 확인하는 모든 값이 1이면 1, 0이면 2, 하나라도 다르면 3
    for i in range(a, a+n):
        for j in range(b, b+n):
            if arr[i][j]=='1' and flag==0:
                flag = 1
            elif arr[i][j]=='1' and flag==2:
                flag = 3
            elif arr[i][j]=='0' and flag==0:
                flag = 2
            elif arr[i][j]=='0' and flag==1:
                flag = 3
        if flag==3:
            break
    if flag==1:
        print('1', end='')
    elif flag==2:
        print('0', end='')
    else:
        print('(', end='') # 하나라도 다르면 4사분면으로 나눠서 재귀 돌리고 겉에 괄호 붙이기
        check(a, b, n//2)
        check(a, b+n//2, n//2)
        check(a+n//2, b, n//2)
        check(a+n//2, b+n//2, n//2)
        print(')', end='')
check(0, 0, N)