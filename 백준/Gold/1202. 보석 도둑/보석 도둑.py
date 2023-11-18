import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())
jewels = []

for _ in range(n):
    weight, money = map(int, input().split())
    jewels.append([weight, money])
jewels.sort()
bagCap = [int(input()) for _ in range(k)]
bagCap.sort()

temp = []
ans = 0
for bag in bagCap:
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(temp,-jewels[0][1])
        heapq.heappop(jewels)
    if temp:
        ans -= heapq.heappop(temp)
print(ans)