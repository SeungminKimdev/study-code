import sys
input = sys.stdin.readline

import heapq
hq = []
n = int(input())
for _ in range(n):
    inNum = int(input())
    if inNum == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(hq))
    else:
        heapq.heappush(hq,inNum * -1)