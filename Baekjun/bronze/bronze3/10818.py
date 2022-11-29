T = int(input())
numbers = list(map(int, input().split()))
max = 0
min = 1000001
for i in range(T):
    if numbers[i] > max:
        max = numbers[i]
for j in range(T):
    if numbers[j] < min:
        min = numbers[j]
print(min, max)
# print(min(numbers), max(numbers))