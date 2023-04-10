import sys
input = sys.stdin.readline

n = int(input())
numList = []
for _ in range(n):
    a,b = map(int,input().split())
    numList.append([b,a])
numList = sorted(numList)
for i in numList:
    print(str(i[1]) + " " + str(i[0]))