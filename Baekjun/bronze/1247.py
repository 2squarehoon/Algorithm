# B3 부호

for _ in range(3):
    n = int(input())
    cnt = 0
    for _ in range(n):
        cnt += int(input())
    if cnt>0:
        print("+")
    elif cnt==0:
        print(0)
    else:
        print("-")