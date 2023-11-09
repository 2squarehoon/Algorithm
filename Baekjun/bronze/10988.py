# B2 팰린드롬인지 확인하기
word = input()
word1 = word[::-1]
if word == word1:
    print(1)
else:
    print(0)