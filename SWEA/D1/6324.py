"""
6324: 8. 함수의 기초 5
"""

def jungbok(lst):
    return sorted(list(set(lst)))

list1 = [1, 2, 3, 4, 3, 2, 1]
print(list1)
print(jungbok(list1))