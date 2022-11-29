A = int(input())
B = int(input())
C = int(input())
T = A * B * C
list1 = []
while T:
    list1.append(T%10)
    T = T//10
for i in range(10):
    print(list1.count(i))
