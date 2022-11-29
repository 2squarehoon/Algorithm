T = int(input())
cnt = 0
for test_case in range(1, T+1):
    word = input()
    cnt += 1
    for letter in word:
        word = word.lstrip(letter)
        if letter in word:
            cnt -= 1
            break
print(cnt)
