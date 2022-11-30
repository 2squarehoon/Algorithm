def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

M, N = map(int, input().split())
for i in range(M, N+1):
    if isPrime(i):
        print(i)



# for i in range(M, N+1):
#     cnt = 0
#     for j in range(1, i+1):
#         if not i % j:
#             cnt += 1
#     if cnt == 2:
#         print(i)
        # 시간이슈...