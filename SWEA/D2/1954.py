"""
1954: 달팽이 숫자
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    di = [1, 0, -1, 0] # 방향을 설정하는 델타값, 순서대로 우 하 좌 상
    dj = [0, 1, 0, -1]
    ni = 0 # 반복문이 시작되면서 델타값이 더해지기 때문에 -1을 해줬지만 값을 채워나갈 array에 껍데기를 씌워놔서 인덱스값을 1 추가해야함.
    nj = 1
    k = 0
    arr = [[1]*(N+2)] + [[1] + [0]*N + [1] for _ in range(N)] + [[1]*(N+2)]
    # 방향을 바꾸는 조건문에 다음 칸으로 이동했을 때 0이 아니라면 방향을 바꾸는 조건문을 만들기 위해 껍데기를 생성
    for n in range(1, N**2 + 1):
        ni += di[k]
        nj += dj[k]
        arr[nj][ni] = n
        if k == 0 and arr[nj][ni+1] != 0:
            k = 1
        if k == 1 and arr[nj+1][ni] != 0:
            k = 2
        if k == 2 and arr[nj][ni-1] != 0:
            k = 3
        if k == 3 and arr[nj-1][ni] != 0:
            k = 0
    print(f'#{tc}')
    for y in range(1, N+1):
        for x in range(1, N+1):
            print(arr[y][x], end=' ')
        print('')