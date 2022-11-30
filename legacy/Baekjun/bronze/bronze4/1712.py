import math
a, b, c = map(int, input().split())
x = 0
if b >= c:
    x = -1
elif a%(c-b) == 0:
    x = a//(c-b) + 1
else:
    x = math.ceil(a/(c-b))
print(x)