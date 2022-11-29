"""
6276: [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 3
"""

lst = []
a = 0
for i in range(2, 10):
    lst1 = []
    for j in range(1, 10):
        a = i*j
        if not (a % 3 == 0 or a % 7 == 0):
        	lst1.append(a)
    lst.append(lst1)
    
print(lst)