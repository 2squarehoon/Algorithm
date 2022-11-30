numbers = list(map(int, input().split()))
sum1 = 0
for i in range(len(numbers)):
    sum1 += numbers[i] ** 2
print(sum1%10)
