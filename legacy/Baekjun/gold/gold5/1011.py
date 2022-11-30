T = int(input())
for test_case in range(1, T+1):
    x, y = map(int, input().split())
    d = y-x
    if d <= 3:
        print(d)
    d = d - 2
    cnt = 2

    # 이 이후로는 내 능력 밖이다.