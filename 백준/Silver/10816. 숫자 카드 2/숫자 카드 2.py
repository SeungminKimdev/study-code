import sys
input = sys.stdin.readline

numdict = {}
N = int(input())
numList = input().split()
for i in numList:
    if i in numdict:
        numdict[i] += 1
    else:
        numdict[i] = 1
M = int(input())
findNum = input().split()
answer = []
for i in findNum:
    if i in numdict:
        answer.append(numdict[i])
    else:
        answer.append(0)
print(*answer)