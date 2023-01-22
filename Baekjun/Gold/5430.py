# G5 AC
import sys
input = sys.stdin.readline
from collections import deque

K = int(input())
for tc in range(K):
    p = input()
    n = int(input())
    arr = deque(input()[1:-2].split(','))
    if not n:
        arr = []
    flag = 0
    for f in p:
        if f == 'R':
            flag += 1
        elif f == 'D':
            if not arr:
                print('error')
                break
            else:
                if flag % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    else:
        if flag %2:
            arr.reverse()
            print('['+','.join(arr)+']')
        else:
            print('['+','.join(arr)+']')
