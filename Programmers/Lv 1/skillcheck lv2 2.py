def solution(numbers, target):
    arr = [0]*1001
    cnt = sum(numbers)
    for i in range(1<<len(numbers)):
        lst = []
        for j in range(len(numbers)):
            if i & (1<<j):
                lst.append(numbers[j])
        temp = cnt-sum(lst)*2
        if temp >= 1:
            arr[temp] += 1
    return arr[target]
