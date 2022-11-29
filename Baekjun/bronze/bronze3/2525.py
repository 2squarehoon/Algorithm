a, b = map(int, input().split())
plus = int(input())
plusH, m = divmod(b+plus, 60)
h = (a+plusH)%24
print(f'{h} {m}')