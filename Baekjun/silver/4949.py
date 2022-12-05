# S4 균형잡힌 세상
import sys
input = sys.stdin.readline
from collections import deque
while True:
    sentence = list(map(str, input()))[0:-1]
    stack = deque()
    if sentence == ['.']:
        break
    ans = 'yes'
    for alphabet in sentence:
        if alphabet == '(':
            stack.append(alphabet)
        elif alphabet == '[':
            stack.append(alphabet)
        elif alphabet == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                ans = 'no'
                break
        elif alphabet == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                ans = 'no'
                break
    if stack:
        ans = 'no'
    print(ans)