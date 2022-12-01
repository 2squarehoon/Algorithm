# S5 나이순 정렬

N = int(input())
lst = []
for _ in range(N):
    age, name = map(str, input().split())
    age = int(age)
    lst.append((age, name))
lst.sort(key=lambda x: x[0])
for i in range(N):
    print(*lst[i])