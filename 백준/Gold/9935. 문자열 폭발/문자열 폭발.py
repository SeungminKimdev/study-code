import sys
input = sys.stdin.readline

s = input().rstrip()
boom = input().rstrip()
boomLen = len(boom)
stack = []

for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-boomLen:]) == boom:
        for _ in range(boomLen):
            stack.pop()

if stack:
    print(*stack,sep='')
else:
    print('FRULA')