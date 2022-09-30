chess = [1,1,2,2,2,8]
inNum = list(map(int,input().split()))
for i,j in zip(chess,inNum):
    print(i-j)