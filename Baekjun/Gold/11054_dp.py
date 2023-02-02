# G4 가장 긴 바이토닉 부분 수열
import sys
input = sys.stdin.readline

N = int(input())
Ai = list(map(int, input().split()))
Aj = Ai[::-1] # 뒤에서부터 증가하는 부분수열 찾기위해 기존 데이터를 뒤집어둠
dp1, dp2 = [0]*N, [0]*N
for i in range(N): # 11053 문제 참조, 앞에서부터 증가하는 부분수열 찾기
    for j in range(i):
        if Ai[i]>Ai[j] and dp1[i]<dp1[j]:
            dp1[i] = dp1[j]
    dp1[i] += 1
for k in range(N): # 뒤에서부터 증가하는 부분수열 찾기
    for l in range(k):
        if Aj[k]>Aj[l] and dp2[k]<dp2[l]:
            dp2[k] = dp2[l]
    dp2[k] += 1
ans = 0
dp2 = dp2[::-1] # 다시 뒤집어줘야 위치값을 맞출 수 있음
for x in range(N):
    if ans < dp1[x]+dp2[x]:
        ans = dp1[x]+dp2[x]
print(ans-1)