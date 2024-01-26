import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int,input().split())
chicken = []
house = []
for i in range(n):
    temp = input().split()
    for j in range(n):
        if temp[j] == '1':
            house.append((i,j))
        elif temp[j] == '2':
            chicken.append((i,j))

ans = 1e8
nCm = list(combinations(chicken,m))
for i in nCm:
    tempSum = 0
    for x,y in house:
        tempLen = 1e8
        for chiX, chiY in i:
            length = abs(x-chiX) + abs(y-chiY)
            tempLen = min(tempLen,length)
        tempSum += tempLen
    ans = min(ans,tempSum)
print(ans)