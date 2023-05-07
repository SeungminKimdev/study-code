import sys
input = sys.stdin.readline

pocketIn, order = map(int,input().split())
pocketDict = {}

for i in range(1,pocketIn+1):
    tempPk = input().strip()
    pocketDict[str(i)] = tempPk
    pocketDict[tempPk] = i

for _ in range(order):
    inputO = input().strip()
    print(pocketDict[inputO])