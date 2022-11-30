C = int(input())
for test_case in range(1, C+1):
    grades = list(map(int, input().split()))
    N = grades.pop(0)
    cnt = 0
    for i in range(N):
        if grades[i] > sum(grades)/N:
            cnt += 1
    rates = (cnt*100) / N
    print(f'{rates:.3f}%')

