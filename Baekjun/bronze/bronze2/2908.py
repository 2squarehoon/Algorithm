a, b = map(str, input().split())
A = a[::-1]
B = b[::-1]
print(max(int(A), int(B)))