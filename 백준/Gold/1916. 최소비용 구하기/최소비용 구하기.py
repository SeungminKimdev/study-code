import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())
root = {i:[] for i in range(n)}
for _ in range(m):
    start, end, cost = map(int,input().split())
    root[start-1].append((end-1,cost))
start, end = map(int,input().split())
start -= 1
end -= 1

dis = [1e8] * n
visited = [False] * n
dis[start] = 0

now = start
for _ in range(n-1):
    visited[now] = True
    for next,nextcost in root[now]:
        if dis[next] > nextcost + dis[now]:
            dis[next] = nextcost + dis[now]
    temp = []
    for i in range(n):
        if not visited[i]:
            temp.append((dis[i],i))
    heapq.heapify(temp)
    a,b = heapq.heappop(temp)
    now = b
print(dis[end])