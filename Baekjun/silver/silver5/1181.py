import math
N = int(input())
words = []
numbers = set()
for i in range(N):
    words.append(str(input()))
for word in words:
    cnt = 0
    for j in range(len(word)):
        cnt += (ord(word[j])-96)*(100**(len(word)-j-1))
    numbers.add(cnt)
for number in sorted(numbers):
    string = ''
    x = math.ceil(len(str(number))/2)
    for k in range(x):
        string += chr((number//(100 ** (x - k - 1))) + 96)
        number = number % (100 ** (x - k - 1))
    print(string)
