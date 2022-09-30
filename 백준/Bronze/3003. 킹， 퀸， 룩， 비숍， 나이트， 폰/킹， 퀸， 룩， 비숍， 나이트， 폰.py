chess = [1,1,2,2,2,8]
inNum = list(map(int,input().split()))
answer = ''
for i,j in zip(chess,inNum):
    answer += str(i-j)
    answer += ' '
print(answer[:-1])