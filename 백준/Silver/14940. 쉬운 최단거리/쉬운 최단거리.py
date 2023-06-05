import sys
input = sys.stdin.readline
from collections import deque

def main():
    n, m = map(int,input().split())
    mapDict = {}
    length = []
    targetX = targetY = 0
    for i in range(n):
        mapDict[i] = []
        length.append([0] * m)
        inputLine = list(map(int,input().split()))
        for j in range(m):
            mapDict[i].append(inputLine[j])
            if inputLine[j] == 2:
                targetX = i
                targetY = j
                
    q = deque()
    q.append((targetX,targetY))
    moveX = [0,0,1,-1]
    moveY = [1,-1,0,0]
    while len(q) != 0:
        nowX, nowY = q.popleft()
        nowLen = length[nowX][nowY]
        for i in range(4):
            nextX = nowX + moveX[i]
            nextY = nowY + moveY[i]
            if nextX >= 0 and nextX < n and nextY >= 0 and nextY < m and mapDict[nextX][nextY] == 1 and length[nextX][nextY] == 0:
                length[nextX][nextY] = nowLen + 1
                q.append((nextX,nextY))
                
    for i in range(n):
        for j in range(m):
            if length[i][j] == 0 and mapDict[i][j] == 1:
                length[i][j] = -1
                
    for i in length:
        print(*i,sep=' ')
    return

if __name__ == '__main__':
    main()