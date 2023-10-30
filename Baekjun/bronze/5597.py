# B5 과제 안 내신 분..?
import sys
input = sys.stdin.readline

arr = [n for n in range(1, 31)]
for _ in range(28):
    x = int(input())
    arr.remove(x)
print(arr[0])
print(arr[1])