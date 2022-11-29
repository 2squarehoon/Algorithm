numbers = list(map(int, input().split()))
a = numbers[0]
b = numbers[1]
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')