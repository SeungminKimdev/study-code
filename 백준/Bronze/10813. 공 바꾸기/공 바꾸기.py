import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numList = [i for i in range(1,n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    numList[a-1], numList[b-1] = numList[b-1], numList[a-1]
print(*numList)