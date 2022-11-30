"""
6327: 8. 함수의 기초 8
"""

def sqr(n):
    return n**2
numbers = list(map(int, input().replace(', ',' ').split()))
for num in numbers:
    print(f'square({num}) => {sqr(num)}')