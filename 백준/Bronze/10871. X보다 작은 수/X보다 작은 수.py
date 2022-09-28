N, X = map(int,input().split())
numList = list(map(int,input().split()))

answer = ''
for i in numList:
    if i < X:
        answer += str(i)
        answer += ' '

print(answer[:-1])