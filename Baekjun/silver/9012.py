# S4 괄호

import sys
N = int(sys.stdin.readline())
for _ in range(N):
    ps = list(map(str, sys.stdin.readline()))[0:-1]
    cnt = 0
    stop = False
    for bracket in ps:
        if bracket == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            print('NO')
            stop = True
            break
    if not stop:
        if cnt:
            print('NO')
        else:
            print('YES')