# S4 대칭 차집합
A, B = map(int, input().split())
alst = set(list(map(int, input().split())))
blst = set(list(map(int, input().split())))
print(len(alst) + len(blst) - len(alst&blst)*2)
