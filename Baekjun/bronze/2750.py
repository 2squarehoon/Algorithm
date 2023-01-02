# B2 수 정렬하기

N = int(input())
lst = []
for _ in range(N) :
    lst.append(int(input()))
for i in range(N) :
    for j in range(N) :
        if lst[i] < lst[j] :
            lst[i], lst[j] = lst[j], lst[i]
for n in lst :
    print(n)