# S5 소트인사이드

lst = list(map(int, input()))
lst.sort(reverse=True)
for n in lst:
    print(n, end='')