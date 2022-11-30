T = int(input())
for test_case in range(1, T+1):
    cnt = 0
    list1 = list(str(input()).split('X'))
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            cnt += j+1
    print(cnt)

