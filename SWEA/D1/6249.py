"""
6249: 7. 흐름과 제어 - 반복 - 연습문제 10
"""


num = str(input())
counts = [0]*10
for letter in num:
    for i in range(10):
        if int(letter) == i:
            counts[i] += 1
print(*range(10))
print(*counts)
# packing, unpacking 인자 *랑 친해지자