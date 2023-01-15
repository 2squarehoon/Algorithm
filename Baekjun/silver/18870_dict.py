# S2 좌표 압축
N = int(input())
lst = list(map(int, input().split()))
lst2 = sorted(list(set(lst)))
dic = {lst2[i]:i for i in range(len(lst2))}
for j in lst:
    print(dic[j], end=' ')