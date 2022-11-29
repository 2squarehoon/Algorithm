''' 코드 자체는 오류가 없지만 ㅈㄴ 오래걸려서 오답
def saengsung(n):
    ss = []
    while n < 10000:
        n1 = str(n)
        try:
            for i in range(1, 5):
                n += int(n1[-i])
            ss.append(n)
        except IndexError:
            ss.append(n)
    return ss

numbers = []
for n in range(1, 10001):
    numbers.append(n)
for s in range(1, 10001):
    numbers = [x for x in numbers if x not in saengsung(s)]

print(numbers)
'''
numbers = set()
for n in range(1, 10001):
    numbers.add(n)
ss_numbers = set()
for n in range(1, 10001):
    for j in str(n):
        n += int(j)
    ss_numbers.add(n)
self_numbers = sorted(numbers - ss_numbers)
for number in self_numbers:
    print(number)



