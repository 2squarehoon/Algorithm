N, M = map(int, input().split())
cards = list(map(int, input().split()))
arr = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if cards[i] + cards[j] + cards[k] <= M:
                arr.append(cards[i] + cards[j] + cards[k])
print(max(arr))