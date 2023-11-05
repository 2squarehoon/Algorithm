# S5 LCM
import sys
input = sys.stdin.readline
from math import gcd

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(int(a*b/gcd(a, b)))