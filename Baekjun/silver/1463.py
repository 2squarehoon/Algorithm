# S3 1로 만들기
N = int(input())
lst = [0]*(N+1)
for i in range(2, N+1):
    lst[i] = lst[i-1] + 1
    if not i%3:
        lst[i] = min(lst[i], lst[i//3]+1)
    if not i%2:
        lst[i] = min(lst[i], lst[i//2]+1)
print(lst[N])