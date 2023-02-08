def solution(survey, choices):
    arr = [0]*4
    cnt = len(survey)
    for i in range(cnt):
        if survey[i][0]=='R':
            arr[0] -= choices[i]-4
        elif survey[i][0]=='T':
            arr[0] += choices[i]-4
        elif survey[i][0]=='C':
            arr[1] -= choices[i]-4
        elif survey[i][0]=='F':
            arr[1] += choices[i]-4
        elif survey[i][0]=='J':
            arr[2] -= choices[i]-4
        elif survey[i][0]=='M':
            arr[2] += choices[i]-4
        elif survey[i][0]=='A':
            arr[3] -= choices[i]-4
        else:
            arr[3] += choices[i]-4
    answer = ''
    if arr[0]>=0:
        answer += 'R'
    else:
        answer += 'T'
    if arr[1]>=0:
        answer += 'C'
    else:
        answer += 'F'
    if arr[2]>=0:
        answer += 'J'
    else:
        answer += 'M'
    if arr[3]>=0:
        answer += 'A'
    else:
        answer += 'N'
    return answer