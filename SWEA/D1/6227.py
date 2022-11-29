"""
6227: 6. 흐름과 제어 - If 8
"""
even_num = []
for n in range(100, 288):
    even_num.append(n)
    for odd in range(1, 10, 2):
    	if str(odd) in str(n):
            try:
                even_num.remove(n)
            except ValueError:
                pass
for num in even_num:
    print(num, end=',')
print(288)