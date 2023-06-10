import sys
input = sys.stdin.readline
from collections import deque

def bfs(inputMap, x, y, visited, maxSize):
    q = deque()
    q.append((x,y))
    moveX = [0,0,1,-1]
    moveY = [1,-1,0,0]
    color = inputMap[x][y]
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nextX = x + moveX[i]
            nextY = y + moveY[i]
            if nextX >= 0 and nextX < maxSize and nextY >= 0 and nextY < maxSize:
                if not visited[nextX][nextY] and inputMap[nextX][nextY] == color:
                    visited[nextX][nextY] = True
                    q.append((nextX,nextY))
    return

def colorBfs(inputMap, x, y, visited, maxSize):
    q = deque()
    q.append((x,y))
    moveX = [0,0,1,-1]
    moveY = [1,-1,0,0]
    color = (inputMap[x][y] == 'B')
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nextX = x + moveX[i]
            nextY = y + moveY[i]
            if nextX >= 0 and nextX < maxSize and nextY >= 0 and nextY < maxSize:
                if not visited[nextX][nextY] and (inputMap[nextX][nextY] == 'B') == color:
                    visited[nextX][nextY] = True
                    q.append((nextX,nextY))
    return

def main():
    n = int(input())
    inputMap = {}
    normalVisited = {}
    colorVisited = {}
    for i in range(n):
        inputMap[i] = input().strip()
        normalVisited[i] = [False] * n
        colorVisited[i] = [False] * n
    
    normal = 0
    colorN = 0
    for i in range(n):
        for j in range(n):
            if not normalVisited[i][j]:
                bfs(inputMap, i, j, normalVisited, n)
                normal += 1
            if not colorVisited[i][j]:
                colorBfs(inputMap, i, j, colorVisited, n)
                colorN += 1
    
    print(str(normal) + " " + str(colorN))
    return

if __name__ == '__main__':
    main()