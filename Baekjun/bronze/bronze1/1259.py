while True:
    N = str(input())
    if N == '0':
        break
    x = len(N) // 2
    y = True
    for i in range(x):
        if N[i] != N[-1 * (i+1)]:
            y = False
    if y == True:
        print('yes')
    else:
        print('no')
   
        