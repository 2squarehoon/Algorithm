list1 = []
for test_case in range(9):
    list1.append(int(input()))
max = 0
for i in range(len(list1)):
    if list1[i] > max:
        max = list1[i]
print(max)
print(list1.index(max)+1)