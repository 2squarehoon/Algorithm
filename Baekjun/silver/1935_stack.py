# S3 후위 표기식2
import sys
input = sys.stdin.readline

N = int(input())
arr = input()[0:-1] # 맨 뒤 \n 제거
num_lst = [0]*N
for i in range(N):
    num_lst[i] = int(input())

stack = []
for word in arr:
    if "A" <= word <= "Z":
        stack.append(num_lst[ord(word)-ord("A")])
    else:
        str2 = stack.pop()
        str1 = stack.pop()
        if word == "+":
            stack.append(str1+str2)
        elif word == "-":
            stack.append(str1-str2)
        elif word == "*":
            stack.append(str1*str2)
        else:
            stack.append(str1/str2)
print("%.2f" %stack[0])