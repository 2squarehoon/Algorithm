"""
1966: 숫자를 정렬하자
"""
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = sorted(numbers)
    print(f'#{test_case}', end=' ')
    print(*numbers)