a = int(input())
b = str(input())

num3 = a * int(b[-1])
num4 = a * int(b[-2])
num5 = a * int(b[-3])
num6 = num3 + num4 * 10 + num5 * 100
print(num3)
print(num4)
print(num5)
print(num6)