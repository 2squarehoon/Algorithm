N, K = map(int, input().split())
temper = list(map(int, input().split()))
temps = 0
for i in range(K):
    temps += temper[i]
lst = [temps]
for j in range(N-K):
    temps += temper[j+K]
    temps -= temper[j]
    lst.append(temps)
print(max(lst))
