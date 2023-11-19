# B3 약수 구하기
N, K = map(int, input().split())
arr = []
for i in range(1, N+1):
    if not N%i:
        arr.append(i)
if len(arr) < K:
    print(0)
else:
    print(arr[K-1])