"""
1204: [S/W 문제해결 기본] 1일차 - 최빈수 구하기
"""

T = int(input())
for t in range(T):
    test_case = int(input())
    grades = list(map(int, input().split()))
    jbjg = set(grades)
    counts = dict()
    for score in jbjg:
        counts[score] = grades.count(score)
    print(f'#{test_case} {max([k for k,v in counts.items() if max(counts.values()) == v])}')
        

