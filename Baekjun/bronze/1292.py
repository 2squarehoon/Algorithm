# B1 쉽게 푸는 문제

arr = []
cnt = 0
for i in range(1, 46):
    for j in range(i):
        arr.append(i)

a, b = map(int, input().split())
print(sum(arr[a-1:b]))