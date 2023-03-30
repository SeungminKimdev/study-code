import sys
input = sys.stdin.readline

q = []
n = int(input())
for _ in range(n):
    inStr = input().split()
    command = inStr[0]
    if command == 'push':
        q.append(inStr[1])
    elif command == 'pop':
        if len(q) == 0:
            print('-1')
        else:
            print(q.pop(0))
    elif command == 'size':
        print(len(q))
    elif command == 'empty':
        print(int(len(q) == 0))
    elif command == 'front':
        if len(q) == 0:
            print('-1')
        else:
            print(q[0])
    elif command == 'back':
        if len(q) == 0:
            print('-1')
        else:
            print(q[-1])