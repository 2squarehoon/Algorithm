def gcd(a, b):
    lst = []
    while b > 0:
        a, b = b, a % b
    return a


def solution(arrayA, arrayB):
    answer = 0
    gcd_A, gcd_B = arrayA[0], arrayB[0]

    for a in arrayA:
        gcd_A = gcd(gcd_A, a)
    for b in arrayB:
        gcd_B = gcd(gcd_B, b)

    lst_A, lst_B = [], []
    if gcd_A != 1:
        for i in range(2, gcd_A + 1):
            if not gcd_A % i:
                lst_A.append(i)
    if gcd_B != 1:
        for j in range(2, gcd_B + 1):
            if not gcd_B % j:
                lst_B.append(j)
    if lst_A:
        for a in lst_A:
            for b in arrayB:
                if not b % a:
                    break
            else:
                answer = max(answer, a)
    if lst_B:
        for b in lst_B:
            for a in arrayA:
                if not a % b:
                    break
            else:
                answer = max(answer, b)
    print(lst_A, lst_B)
    return answer