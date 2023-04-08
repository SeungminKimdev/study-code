import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
dq = deque([i for i in range(1,n+1)])

while len(dq) > 1:
    dq.popleft()
    temp = dq.popleft()
    dq.append(temp)
print(dq[0])

#card bbopgi men wie han jang bu ryu