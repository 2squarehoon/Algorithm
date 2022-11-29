N = int(input())
lst = []
width = []
height = []
for n in range(N):
    L, H = map(int, input().split())
    lst.append([L, H])
    width.append(L)
    height.append(H)
max_width = max(width)
max_H = max(height)
max_L = []
arr = [0]*max_width
for i in range(len(lst)):
    arr[lst[i][0]-1] = lst[i][1]
    if lst[i][1] == max_H:
        max_L.append(lst[i][0]-1)
max_L.sort()
cnt = 0
max_left = 0
for j in range(max_L[0]):
    if max_left < arr[j]:
        max_left = arr[j]
    cnt += max_left
max_right = 0
for k in range(max_width-1,max_L[-1],-1):
    if max_right < arr[k]:
        max_right = arr[k]
    cnt += max_right
cnt += max_H * (max_L[-1]-max_L[0]+1)
print(cnt)