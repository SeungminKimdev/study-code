N = int(input())
ans = set(list(map(int,input().split())))
M = int(input())
numList = list(map(int,input().split()))
for i in numList:
    if i in ans:
        print('1')
    else:
        print('0')