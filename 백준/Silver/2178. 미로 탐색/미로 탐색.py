import sys

n, m = map(int, sys.stdin.readline().split())
numList = []
visited = []
for _ in range(n):
    tempStr = sys.stdin.readline().strip()
    numList.append([int(tempStr[i]) for i in range(m)])
    visited.append([False for _ in range(m)])

nextX = [1,0,0,-1]
nextY = [0,1,-1,0]

location = []
location.append([0,0,1])
visited[0][0] = True

while(1):
    temp = location.pop(0)
    nowX = temp[0]
    nowY = temp[1]
    nowCount = temp[2]
    
    if(nowX == n-1 and nowY == m-1):
        print(nowCount)
        break
    else:
        for i in range(4):
            tempX = nowX + nextX[i]
            tempY = nowY + nextY[i]
            if(tempX >= 0 and tempX < n and tempY >= 0 and tempY < m):
                if(numList[tempX][tempY] == 1 and visited[tempX][tempY] == False):
                    location.append([tempX,tempY,nowCount+1])
                    visited[tempX][tempY] = True