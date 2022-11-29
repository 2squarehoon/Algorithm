pieces = list(map(int, input().split()))
right_pieces = [1, 1, 2, 2, 2, 8]
for i in range(6):
    print(right_pieces[i]-pieces[i], end = ' ')