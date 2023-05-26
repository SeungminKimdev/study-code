import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, visited, road):
    if visited[start]:
        return 0
    
    q = deque()
    q.append(start)
    visited[start] = True
    while len(q) != 0:
        tempN = q.pop()
        nextN = road[tempN]
        for i in nextN:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return 1

n,m = map(int,input().split())
road = dict()
visited = dict()

for _ in range(m):
    u, v = map(int, input().split())
    visited[u-1] = False
    visited[v-1] = False
    if (u-1) in road:
        road[u-1].append(v-1)
    else:
        road[u-1] = [v-1]
    if (v-1) in road:
        road[v-1].append(u-1)
    else:
        road[v-1] = [u-1]

ans = n - len(visited.keys())
if m == 0:
    ans = n
else:
    for i in visited.keys():
        ans += bfs(i,visited,road)
print(ans)