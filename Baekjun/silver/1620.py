# S4 포켓몬....
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dict = {}
for i in range(1, N+1):
    pokemon = input().strip()
    dict[i] = pokemon
    dict[pokemon] = i
for _ in range(M):
    word = input().strip()
    if ord(word[0]) >= 65:
        print(dict[word])
    else:
        print(dict[int(word)])