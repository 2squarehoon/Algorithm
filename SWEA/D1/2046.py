"""
2046: 스탬프 찍기
"""

import sys
sys.stdin = open('2046_input.txt')

stamps = int(input())
for i in range(stamps):
    print('#', end = '')