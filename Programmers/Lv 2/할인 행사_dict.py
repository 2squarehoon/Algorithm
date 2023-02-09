def solution(want, number, discount):
    answer = 0
    lst = dict()
    total = sum(number)
    for i in range(len(want)):
        lst[want[i]] = number[i]
    for i in range(len(discount)-total+1):
        temp = dict()
        for j in range(i, i+10):
            if discount[j] in temp:
                temp[discount[j]] += 1
            else:
                temp[discount[j]] = 1
        if lst == temp:
            answer += 1
    return answer