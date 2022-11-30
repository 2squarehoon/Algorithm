"""
6325: 8. 함수의 기초 6
"""
def find(x):
    lst = [2, 4, 6, 8, 10]
    for n in lst:
        if x == n:
            return True
    return False

print([2, 4, 6, 8, 10])
print(f'5 => {find(5)}')
print(f'10 => {find(10)}')


