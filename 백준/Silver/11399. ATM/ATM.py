import sys
input = sys.stdin.readline

n = int(input())
numList = list(map(int,input().split()))
numList.sort()
sum = 0
for i in range(n):
    sum += numList[i] * (n-i)
print(sum)