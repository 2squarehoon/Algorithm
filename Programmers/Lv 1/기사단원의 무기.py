def solution(number, limit, power):
    lst = [0]*number
    for i in range(1, number+1):
        for j in range(1, int(i**0.5)+1):
            if not i%j:
                lst[i-1] += 1
                if j**2 != i:
                    lst[i-1] += 1
    answer = 0
    for n in lst:
        if n > limit:
            answer += power
        else:
            answer += n
    return answer