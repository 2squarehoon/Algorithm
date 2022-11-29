"""
2058: 자릿수 더하기
"""

import sys
sys.stdin = open('2058_input.txt')

number = int(input())
goal = 0
while number:
    goal += number % 10
    number = number // 10
print(goal)
