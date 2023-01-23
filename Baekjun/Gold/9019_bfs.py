# G4 DSLR
# 별짓을 다해도 python으로는 시간초과, pypy로 제출해야 풀림...
import sys
from collections import deque
input = sys.stdin.readline

def D(n):
    return (n*2)%10000
def S(n): # -1 을 10000으로 나눈 나머지는 9999다
    return (n-1)%10000
def L(n): # 문자열 변환 후 정수형 변환하면 시간초과
    front = n%1000
    back = n//1000
    return front*10+back
def R(n):
    front = n%10
    back = n//10
    return front*1000+back

T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    q = deque([(A, '')])
    visited = [0]*10000
    while q:
        num, path = q.popleft()
        if num == B:
            print(path)
            break
        tmp = D(num)
        if not visited[tmp]:
            q.append((tmp, path+'D'))
            visited[tmp] = 1
        tmp = S(num)
        if not visited[tmp]:
            q.append((tmp, path+'S'))
            visited[tmp] = 1
        tmp = L(num)
        if not visited[tmp]:
            q.append((tmp, path+'L'))
            visited[tmp] = 1
        tmp = R(num)
        if not visited[tmp]:
            q.append((tmp, path+'R'))
            visited[tmp] = 1
