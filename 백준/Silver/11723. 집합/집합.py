import sys
input = sys.stdin.readline

S = set()
n = int(input())
for _ in range(n):
    inputS = input().split()
    if len(inputS) == 1:
        if inputS[0] == "all":
            S = set([i for i in range(1,21)])
        else:
            S = set()
        continue
    
    command = inputS[0]
    target = int(inputS[1])
    if command == "add":
        S.add(target)
    elif command == "check":
        if target in S:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if target in S:
            S.discard(target)
        else:
            S.add(target)
    elif command == "remove":
        S.discard(target)
