"""
6321: 8. 함수의 기초 3
"""
def sosu(n):
    cnt = 0
    for i in range(1, n+1):
        if not n % i:
            cnt += 1
    if cnt <= 2:
        return '소수입니다.'
    else:
        return '소수가 아닙니다.'
num = int(input())
print(sosu(num))