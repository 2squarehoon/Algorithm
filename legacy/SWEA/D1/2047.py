"""
2047: 신문 헤드라인
"""

import sys
sys.stdin = open('2047_input.txt')

head = list(input())
upper_head = ''
for i in range(len(head)):
    if ord(head[i]) > 96:
        head[i] = chr(ord(head[i]) - 32)
head = ''.join(head)
print(head)

# print(ord('z'), ord('Z'), ord('_'), ord('.'))