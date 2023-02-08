def solution(k, score):
    arr = []
    answer = []
    for s in score:
        arr.append(s)
        arr.sort()
        if len(arr)<=k:
            answer.append(min(arr))
        else:
            arr = arr[1:k+1]
            answer.append(min(arr))
    return answer