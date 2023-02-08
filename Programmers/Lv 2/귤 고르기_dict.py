def solution(k, tangerine):
    arr = dict()
    for t in tangerine:
        if t in arr:
            arr[t] += 1
        else:
            arr[t] = 1
    answer = 0
    arr = sorted(arr.items(), key=lambda item: item[1], reverse=True)
    cnt = 0
    for i in range(len(arr)):
        cnt += arr[i][1]
        answer += 1
        if cnt >= k:
            break
    return answer