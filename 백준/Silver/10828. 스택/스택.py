import sys
N = int(input())
save = list()
for i in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        save.append(order[1])
    elif order[0] == 'pop':
        if len(save) == 0:
            print('-1')
        else:
            print(save.pop())
    elif order[0] == 'size':
        print(len(save))
    elif order[0] == 'empty':
        if len(save) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(save) == 0:
            print('-1')
        else:
            print(save[-1])