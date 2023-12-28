import sys
input = sys.stdin.readline
import copy

n = int(input())
mainSpace = []
visited = []
dx = [-1,0,0,1]
dy = [0,-1,1,0]
for i in range(n):
    temp = list(map(int,input().split()))
    mainSpace.append([])
    visited.append([False]*n)
    for j in range(n):
        if temp[j] == 9:
            shark = (i,j)
            visited[i][j] = True
            temp[j] = 0
        mainSpace[i].append(temp[j])

size = 2
eat = 0
day = 0
while True:
    space = copy.deepcopy(mainSpace)
    q = []
    q.append(shark)
    search = False
    length = 1
    use = 0
    tempD = 0
    searchq = []
    while q:
        nowX, nowY = q.pop(0)
        space[nowX][nowY] = -1
        for i in range(4):
            nextX = nowX + dx[i]
            nextY = nowY + dy[i]
            if nextX >= 0 and nextX < n and nextY < n and nextY >= 0:
                if space[nextX][nextY] > size:
                    continue
                if space[nextX][nextY] == 0 or space[nextX][nextY] == size:
                    q.append((nextX,nextY))
                    space[nextX][nextY] = -1
                elif 0 < space[nextX][nextY] < size and visited[nextX][nextY] != True:
                    searchq.append((nextX,nextY))
                    search = True
        use += 1
        if use == length:
            if search:
                nextX,nextY = min(searchq)
                visited[nextX][nextY] = True
                mainSpace[nextX][nextY] = 0
                eat += 1
                if eat == size:
                    eat = 0
                    size += 1
                day += 1 + tempD
                shark = (nextX,nextY)
                break
            tempD += 1
            use = 0
            length = len(q)
            q.sort()
    if not search:
        break
print(day)