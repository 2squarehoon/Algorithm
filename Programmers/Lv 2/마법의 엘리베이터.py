def solution(storey):
    answer = 0
    while storey:
        r = storey % 10
        if r>5:
            storey += 10-r
            answer += 10-r
        elif r<5:
            storey -= r
            answer += r
        else:
            if (storey//10) % 10 > 4:
                storey += 10
            answer += r
        storey = storey//10
    return answer