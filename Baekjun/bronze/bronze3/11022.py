T = int(input())
for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))
    a = numbers[0]
    b = numbers[1]
    print(f'Case #{test_case}: {a} + {b} = {a+b}')