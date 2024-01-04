# B2 TV 크기
D, H, W = map(int,input().split())
print(int(((D**2)*(H**2)/((H**2)+(W**2)))**0.5), end=" ")
print(int(((D**2)*(W**2)/((H**2)+(W**2)))**0.5))
