nx = list(map(int, input().split()))
N = nx[0]
X = nx[1]
numbers = list(map(int, input().split()))
for i in range(N):
    if numbers[i] < X:
        print(numbers[i], end = ' ')