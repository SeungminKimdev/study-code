import sys
input = sys.stdin.readline
from collections import deque

def swanBfs(lake,visited,q,nq):
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    while q:
        nowX, nowY = q.popleft()
        for i in range(4):
            nextX = nowX + dx[i]
            nextY = nowY + dy[i]
            if nextX >= 0 and nextX < r and nextY >= 0 and nextY < c:
                if not visited[nextX][nextY]:
                    if lake[nextX][nextY] == 'L':
                        return True
                    elif lake[nextX][nextY] == 'X':
                        visited[nextX][nextY] = True
                        nq.append((nextX,nextY))
                    else: #lake[nextX][nextY] = '.'
                        visited[nextX][nextY] = True
                        q.append((nextX,nextY))
    return False

def bfs(lake,visited,q,nq):
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    while q:
        nowX, nowY = q.popleft()
        for i in range(4):
            nextX = nowX + dx[i]
            nextY = nowY + dy[i]
            if nextX >= 0 and nextX < r and nextY >= 0 and nextY < c:
                if not visited[nextX][nextY] and lake[nextX][nextY] == 'X':
                    lake[nextX][nextY] = '.'
                    nq.append((nextX,nextY))

r,c = map(int,input().split())
lake = []
visited = []
dq = deque()
swansQ = deque()
nswansQ = deque()
ndq = deque()

for i in range(r):
    visited.append([False] * c)
    lake.append([])
    tempIn = input().rstrip()
    for j in range(c):
        if tempIn[j] == 'L':
            swans = (i,j)
        lake[i].append(tempIn[j])
        if tempIn[j] != 'X':
            dq.append((i,j))

swansQ.append(swans)
visited[swans[0]][swans[1]] = True
find = False
day = 0
while not find:
    find = swanBfs(lake,visited,swansQ,nswansQ)
    if not find:
        bfs(lake,visited,dq,ndq)
        dq = ndq
        swansQ = nswansQ
        ndq = deque()
        nswansQ = deque()
        day += 1
print(day)