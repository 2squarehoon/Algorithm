word = str(input()).lower()
letters = []
for i in range(len(word)):
    letters.append(word[i])
count_letter = dict()
for n in range(97, 123):
    count_letter[chr(n)] = letters.count(chr(n))
max_letter = [k for k,v in count_letter.items() if max(count_letter.values()) == v]
if len(max_letter) > 1:
    print('?')
else:
    print(max_letter[0].upper())