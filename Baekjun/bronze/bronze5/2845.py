party = list(map(int, input().split()))
L = party[0]
P = party[1]
pred_n = L*P
numbers = list(map(int, input().split()))
for i in range(len(numbers)):
    print(numbers[i]-pred_n, end = ' ')