# B1 진법 변환 2
N, B = map(int, input().split())
array = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lst = []
while N != 0:
    lst.append(N%B)
    N = N // B
lst = lst[::-1]
ans = ""
for n in lst:
    ans += array[n]
print(ans)