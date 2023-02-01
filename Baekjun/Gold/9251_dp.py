# G5 LCS
import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
l1, l2 = len(str1), len(str2)
arr = [[0]*(l2+1) for _ in range(l1+1)]
for i in range(1, l1+1):
    for j in range(1, l2+1):
        if str1[i-1]==str2[j-1]:
            arr[i][j] = arr[i-1][j-1]+1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
print(arr[l1][l2])