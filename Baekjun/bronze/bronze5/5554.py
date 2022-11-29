HS = int(input())
SP = int(input())
PA = int(input())
AH = int(input())
sum1 = HS + SP + PA + AH
x = sum1 // 60
y = sum1 % 60
print(f'{x}\n{y}')