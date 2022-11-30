def bsort(lst):  # 버블정렬 구현
    lst1 = lst[::] # 원본을 수정하지 않기 위해 깊은 복사 사용
    for i in range(len(lst1) - 1, 0, -1):
        for j in range(i):
            if lst1[j] > lst1[j+1]:
                lst1[j], lst1[j+1] = lst1[j+1], lst1[j]
    return lst1

def garo(lst):  # 가로 숫자들 검증 + 그냥 숫자들 검증
    for x in range(9):
        if bsort(lst[x]) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:  # 정렬된 숫자가 123456789와 같으면 True, 아니면 False
            return False
    return True

def sero(lst):  # 세로 숫자들 검증
    lst1 = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            lst1[i][j] = lst[j][i]
    return garo(lst1)

def square(lst):  # 리스트를 3*3 정사각형 기준으로 묶어서 새로 만듦, 순서는 좌측 상단부터 오른쪽으로
    lst2 = [[0] * 9 for _ in range(9)]
    x = y = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    lst2[y][x] = lst[i * 3 + k][j * 3 + l]
                    x += 1
            x = 0
            y += 1
    return garo(lst2)

T = int(input())
for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{test_case} {int(garo(sudoku) and sero(sudoku) and square(sudoku))}')
