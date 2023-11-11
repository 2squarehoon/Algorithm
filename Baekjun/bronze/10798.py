# B1 세로읽기

text = []
for i in range(5):
    text.append(input())

for i in range(max(len(e) for e in text)): # text중 가장 긴 문자열만큼
    for j in range(5):
        if i < len(text[j]):
            print(text[j][i], end='')

