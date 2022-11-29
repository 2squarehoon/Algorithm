def hansu(n):
    if n < 100:
        return n
    elif n >= 100 and n <= 999:
        cnt = 99
        for num in range(100, n+1):
            a = int(str(num)[0])
            b = int(str(num)[1])
            c = int(str(num)[2])
            if a + c == b * 2:
                cnt +=1
        return cnt
    else:
        return hansu(999)
n = int(input())
print(hansu(n))