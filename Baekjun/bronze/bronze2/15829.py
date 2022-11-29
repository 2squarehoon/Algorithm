L = int(input())
str1 = str(input())
cnt = 0
for i in range(L):
    cnt += (ord(str1[i]) - 96) * (31**i)
print(cnt%1234567891)