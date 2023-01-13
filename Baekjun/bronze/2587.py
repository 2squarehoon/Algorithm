# B2 대표값 2
lst = []
cnt = 0
for _ in range(5):
    n = int(input())
    lst.append(n)
    cnt += n
lst.sort()
print(cnt//5)
print(lst[2])
