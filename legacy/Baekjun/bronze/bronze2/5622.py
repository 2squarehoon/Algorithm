word = str(input())
dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
cnt = 0
for i in range(len(word)):
    for dial in dials:
        if word[i] in dial:
            cnt += dials.index(dial) + 3
print(cnt)