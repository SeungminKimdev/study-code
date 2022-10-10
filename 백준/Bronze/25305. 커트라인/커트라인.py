import sys
N, k = map(int, sys.stdin.readline().split())
numList = list(map(int,sys.stdin.readline().split()))
numList.sort(reverse=True)
print(numList[k-1])