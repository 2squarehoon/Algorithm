def solution(num, total):
    answer = []
    if num%2:
        for i in range(num):
            answer.append(total//num+i-num//2)
    else:
        for i in range(num):
            answer.append(total//num+i+1-num//2)
    return answer