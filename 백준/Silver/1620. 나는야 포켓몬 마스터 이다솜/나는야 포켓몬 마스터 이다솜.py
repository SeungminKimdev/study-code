import sys
input = sys.stdin.readline

pocketIn, order = map(int,input().split())
pocketNum = []
pocketDict = {}

for i in range(1,pocketIn+1):
    tempPk = input().strip()
    pocketNum.append(tempPk)
    pocketDict[tempPk] = i

for _ in range(order):
    inputO = input().strip()
    try:
        num = int(inputO)
        print(pocketNum[num-1])
    except:
        print(pocketDict[inputO])