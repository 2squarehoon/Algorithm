# S2 A->B
A, B = map(int, input().split())
ans = 1
while (A!=B):
    ans += 1
    temp = B
    if B%10 == 1:
        B = (B-1)//10
    elif not B%2:
        B = B//2
    if temp == B: # 두 연산을 수행해도 값의 변화가 없다면 무한루프
        print(-1)
        break
else:
    print(ans)