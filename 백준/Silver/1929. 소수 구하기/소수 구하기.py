import sys
M, N = map(int, sys.stdin.readline().split())
numList = [i % 2 != 0 for i in range(N+1)]
numList[1] = False
numList[2] = True
for i in range(3,N+1):
    if numList[i]:
        tempNum = i * 2
        while tempNum < N+1:
            numList[tempNum] = False
            tempNum += i
for i in range(M,N+1):
    if numList[i]:
        print(i)