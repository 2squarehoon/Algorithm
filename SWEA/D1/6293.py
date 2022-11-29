import math
numbers = list(map(int, input().split(', ')))
won = [x * 2 * math.pi for x in numbers]
print(f'{won[0]:0.2f}, {won[1]:0.2f}, {won[2]:0.2f}, {won[3]:0.2f}')