import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numList = [i for i in range(1,n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    temp = numList[a-1:b]
    temp = reversed(temp)
    numList[a-1:b] = temp
print(*numList)