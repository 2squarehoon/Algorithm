# B3 삼각형과 세 변
while True:
    numbers = list(map(int, input().split()))
    numbers.sort()
    a, b, c = numbers[0], numbers[1], numbers[2]
    if a==0 and b==0 and c==0:
        break
    if a==b==c:
        print("Equilateral")
    elif c >= a + b:
        print("Invalid")
    elif a==b or b==c:
        print("Isosceles")
    else:
        print("Scalene")
