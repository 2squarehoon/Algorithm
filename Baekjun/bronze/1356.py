# B1 유진수

n = str(input())
flag = False
for i in range(1, len(n)):
    a, b = n[:i], n[i:]
    c, d = 1, 1
    for x in a:
        c *= int(x)
    for y in b:
        d *= int(y)
    if c==d:
        flag = True
        break
if flag:
    print("YES")
else:
    print("NO")