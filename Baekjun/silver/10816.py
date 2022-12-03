# S4 숫자 카드 2
import sys
N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
dict = {}
for card in cards:
    if card in dict:
        dict[card] += 1
    else:
        dict[card] = 1

for number in numbers:
    cnt = dict.get(number)
    if not cnt:
        print(0, end=" ")
    else:
        print(cnt, end=" ")