T = int(input())
for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))
    print(f'Case #{test_case}: {numbers[0] + numbers[1]}')