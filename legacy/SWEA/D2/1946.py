"""
1946: 간단한 압축풀기
"""

T = int(input())
for test_case in range(1, T+1):
    print(f'#{test_case}')
    N = int(input())
    letters = dict()
    for i in range(N):
        letter, count = map(str, input().split())
        letters[letter] = int(count)
    cnt = 0
    for n in letters:
        for j in range(letters[n]):
            print(n, end='')
            cnt += 1
            if cnt == 10:
                print('')
                cnt = 0
    print('')
    