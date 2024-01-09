# B2 부재중 전화

N, L, D = map(int, input().split())

total = N*L+(N-1)*5
arr = [0]*total
for i in range(0, total, L+5):
    for j in range(i, i+L):
        arr[j] = 1
for i in range(0, total, D):
    if not arr[i]:
        print(i)
        break
else:
    print(i + D)
