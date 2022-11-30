"""
6328: 8. 함수의 기초 9
"""
def longer(lst):
    if len(lst[0]) >= len(lst[1]):
        return lst[0]
    else:
        return lst[1]

words = list(map(str, input().replace(', ',' ').split()))
print(longer(words))
