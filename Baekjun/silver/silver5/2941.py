word = str(input())
c_alphabets = ['c=', 'c-', 'd-','dz=', 'lj', 'nj', 's=', 'z=']
for alphabet in c_alphabets:
    word = word.replace(alphabet, '*')
print(len(word))

