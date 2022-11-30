for _ in range(4):
    x11, y11, x12, y12, x21, y21, x22, y22 = map(int, input().split())
    if x12<x21 or x11>x22 or y12<y21 or y11>y22:
        print('d')
    else:
        cnt = 0
        if x12 == x21:
            cnt += 1
        if y12 == y21:
            cnt += 1
        if x11 == x22:
            cnt += 1
        if y11 == y22:
            cnt += 1
        if cnt == 2:
            print('c')
        elif cnt == 1:
            print('b')
        else:
            print('a')
