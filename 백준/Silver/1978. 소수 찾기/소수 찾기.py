import sys
N = int(sys.stdin.readline())
inputNum = list(map(int,sys.stdin.readline().split()))
numList = [True for _ in range(1001)]
numList[1] = False
for i in range(2, 1001):
    if numList[i]:
        for j in range(i*2,1001,i):
            numList[j] = False
ans = 0
for i in inputNum:
    if numList[i]:
        ans += 1
print(ans)