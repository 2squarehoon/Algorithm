"""
2050: 알파벳을 숫자로 변환
"""

import sys
sys.stdin = open('2050_input.txt')

alphabets = str(input())
for i in range(len(alphabets)):
    print(ord(alphabets[i]) - 64, end = ' ')