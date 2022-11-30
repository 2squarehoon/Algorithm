number = int(input())
x = 0
while x*(x+1)*3+1 < number:
    x += 1
print(x+1) 