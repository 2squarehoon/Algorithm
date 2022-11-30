"""
2005: 파스칼의 삼각형
"""
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    pascal = [[1], [1,1]]
    for i in range(2, N) :
        list = [1]
        for j in range(i-1) :
            list += [pascal[i-1][j] + pascal[i-1][j+1]]
        list += [1]
        pascal += [list]

    print(f"#{test_case}")
    for i in range(N):
        print('')
        for j in range(len(pascal[i])):
            print(pascal[i][j], end = ' ')
        


         
import sys
sys.stdin = open('2005_input.txt')

