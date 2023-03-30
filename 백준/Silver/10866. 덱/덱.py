import sys
input = sys.stdin.readline

from collections import deque

dq = deque()

n = int(input())
for _ in range(n):
    inStr = input().split()
    command = inStr[0]
    if command == 'push_front':
        dq.appendleft(inStr[1])
    elif command == 'push_back':
        dq.append(inStr[1])
    elif command == 'pop_front':
        if len(dq) == 0:
            print('-1')
        else:
            print(dq.popleft())
    elif command == 'pop_back':
        if len(dq) == 0:
            print('-1')
        else:
            print(dq.pop())
    elif command == 'size':
        print(len(dq))
    elif command == 'empty':
        print(int(len(dq) == 0))
    elif command == 'front':
        if len(dq) == 0:
            print('-1')
        else:
            print(dq[0])
    elif command == 'back':
        if len(dq) == 0:
            print('-1')
        else:
            print(dq[-1])