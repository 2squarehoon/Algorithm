T = int(input())
for test_case in range(1, T+1):
    r, S = map(str, input().split())
    R = int(r)
    letters =[]
    for i in range(len(S)):
        for j in range(R):
            letters.append(S[i])
    print(f"{''.join(letters)}")
