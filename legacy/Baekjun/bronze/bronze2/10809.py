word = str(input())
letters = []
for i in range(len(word)):
    letters.append(word[i])

for n in range(97, 123):
    try:
        print(letters.index(chr(n)), end = ' ')
    except ValueError:
        print(-1, end = ' ')