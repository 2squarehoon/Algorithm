# B2 진법 변환
N, b = input().split()
array = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1]
result = 0

for i,n in enumerate(N):
    result += (int(b)**i)*(array.index(n))
print(result)
