import sys
input = sys.stdin.readline

stack = []
n = int(input())
numList = [int(input()) for i in range(n)]


answer = []
numIn = 1
for i in numList:
    if len(stack) == 0 and numIn > i:
        answer = ['NO']
        break
    if len(stack) != 0:
        if stack[-1] > i:
            answer = ['NO']
            break
        elif stack[-1] == i:
            stack.pop()
            answer.append('-')
            continue
    while numIn != i:
        stack.append(numIn)
        answer.append('+')
        numIn += 1
    answer += ['+','-']
    numIn += 1
print('\n'.join(answer))