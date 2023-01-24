# S2 잃어버린 괄호
import sys
input = sys.stdin.readline

line = input().split('-')
forms = []
for nums in line:
    num = sum(list(map(int, nums.split('+'))))
    forms.append(int(num))
ans = forms[0]
for i in range(1, len(forms)):
    ans -= int(forms[i])
print(ans)