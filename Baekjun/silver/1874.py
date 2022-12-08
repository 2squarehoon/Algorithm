# S3 스택 수열
import sys
input = sys.stdin.readline

N = int(input())
stack = []
ans = []
cur = 1
flag = True
for _ in range(N):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        ans.append('+')
        cur += 1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        print('NO')
        flag = False
        break
if flag:
    for i in ans:
        print(i)
    