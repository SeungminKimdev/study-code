import sys
input = sys.stdin.readline

from heapq import heappush, heappop
minq = [] #중간 값보다 작은 값(내림차순)
maxq = [] #중간 값보다 큰 값(오름차순)
N = int(input())
middle = int(input())
print(middle)

for i in range(2,N+1):
    inputNum = int(input())
    if inputNum < middle:
        heappush(minq,(-inputNum,inputNum))
    else:
        heappush(maxq,(inputNum,inputNum))
    minLen = len(minq)
    maxLen = len(maxq)
    if i % 2 == 0: #짝수개 dog
        if minLen > maxLen:
            heappush(maxq,(middle,middle))
            middle = heappop(minq)[1]
    else: #홀수개
        if minLen < maxLen:
            heappush(minq,(-middle,middle))
            middle = heappop(maxq)[1]
        elif minLen > maxLen:
            heappush(maxq,(middle,middle))
            middle = heappop(minq)[1]
    print(middle)