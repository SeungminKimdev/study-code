import sys
input = sys.stdin.readline

def makeAns(k,n):
    numList = [i for i in range(1,n+1)]
    for _ in range(k):
        for j in range(1,n):
            numList[j] += numList[j-1]
    return numList[n-1]

n = int(input())
for _ in range(n):
    k = int(input())
    n = int(input())
    print(makeAns(k,n))