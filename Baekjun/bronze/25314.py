# B5 코딩은 체육과목 입니다
import sys
input = sys.stdin.readline

N = int(input())
S = "int"
for i in range(N//4):
    S = "long " + S
print(S)