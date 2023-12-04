import sys
input = sys.stdin.readline

n = int(input())
numList = list(map(int,input().split()))
numList.sort()
print(numList[0] * numList[-1])