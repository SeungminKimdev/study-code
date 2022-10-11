import sys
N, M = map(int, sys.stdin.readline().split())
numList = list(map(int,sys.stdin.readline().split()))
sum = 0
for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            tempSum = numList[i] + numList[j] + numList[k]
            if tempSum > sum and tempSum <= M:
                sum = tempSum
print(sum)