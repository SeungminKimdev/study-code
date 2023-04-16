import sys
input = sys.stdin.readline

stack = []
n = int(input())
numList = [int(input()) for i in range(n)]
answer = []
numIn = 1
for i in numList:
    if len(stack) == 0:
        if numIn > i:
            answer = ['NO']
            break
        while numIn != i:
            stack.append(numIn)
            answer.append('+')
            numIn += 1
        answer += ['+','-']
        numIn += 1
    else:
        if stack[-1] > i:
            answer = ['NO']
            break
        elif stack[-1] == i:
            stack.pop()
            answer.append('-')
        else:
            while numIn != i:
                stack.append(numIn)
                answer.append('+')
                numIn += 1
            answer += ['+','-']
            numIn += 1
for i in answer:
    print(i)