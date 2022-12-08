# S3 프린터 큐
import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
for _ in range(n):
    N, M = map(int, input().split())
    imp = deque(list(map(int, input().split())))
    ans = 0
    while imp:
        best = max(imp)
        front = imp.popleft()
        M -= 1
        if best == front:
            ans += 1
            if M < 0:
                print(ans)
                break
            # 최대값이면 pop하고 프린트한 수 1 증가
        else:
            imp.append(front)
            if M < 0:
                M = len(imp) - 1
            # 최대값이 아니면 pop해서 다시 뒤로 붙임