"""
1288: 새로운 불면증 치료법
"""
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    N1 = N # 반복문 실행하면서 입력했던 N자체가 바뀌어버리는거 방지
    numbers = set()
    cnt = 0
    while not len(numbers) == 10:
        for n in str(N):
           numbers.add(n)
        cnt += 1
        N += N1
    print(f'#{test_case} {cnt*N1}')