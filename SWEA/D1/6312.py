"""
6312: 9. 내장함수 5
"""
def function(*T):
    a = 1
    T = int()
    for n in T:
        a *= n
    return a

try:
    print(function(1, 2, '3', 4))
except:
    print('에러발생')