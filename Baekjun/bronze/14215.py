# B3 세 막대

arr = list(map(int, input().split()))
arr.sort()
if arr[2]>=arr[1]+arr[0]:
    print((arr[1]+arr[0])*2-1)
else:
    print(sum(arr))