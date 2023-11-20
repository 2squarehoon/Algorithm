# B1 약수들의 합

while True:
    n = int(input())
    if n == -1:
        break
    lst = []
    for i in range(1, n//2+1):
        if not n%i:
            lst.append(i)
    if sum(lst) == n:
        print(n, end=" = ")
        for j in range(len(lst)):
            print(lst[j], end="")
            if not j == len(lst)-1:
                print(" + ", end="")
        print()
    else:
        print(n, end=" is NOT perfect.")
        print()
