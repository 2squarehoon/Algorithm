"""
1928: Base64 Decoder
"""

T = int(input())
for test_case in range(1, T+1):
    str1 = str(input())
    lst = []
    for i in range(len(str1)//4):
        lst.append(str1[i*4:(i+1)*4])
    # 이게 머선 말이고;;; 서랜

