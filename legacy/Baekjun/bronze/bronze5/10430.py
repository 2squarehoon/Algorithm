numbers = list(map(int, input().split()))
a = numbers[0]
b = numbers[1]
c = numbers[2]
first = (a+b)%c
second = ((a%c) + (b%c))%c
third = (a*b)%c
fourth = ((a%c) * (b%c))%c
print(f'{first}\n{second}\n{third}\n{fourth}')