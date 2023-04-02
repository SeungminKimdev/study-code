import sys
input = sys.stdin.readline

n = int(input())
numList = []
for _ in range(n):
    a, b = map(int,input().split())
    numList.append([a,b])
numList.sort()
for i in numList:
    print(str(i[0]) + " " + str(i[1]))