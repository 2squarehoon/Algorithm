# B1 약수

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr[0]*arr[-1])
