import sys
input = sys.stdin.readline
from collections import deque

def main():
    n, m = map(int,input().split())
    mapDict = {}
    length = {}
    targetX = targetY = 0
    for i in range(n):
        length[i] = [0] * m
        mapDict[i] = list(input().strip().split())
        for j in range(m):
            if mapDict[i][j] == '2':
                targetX = i
                targetY = j
                
    q = deque()
    q.append((targetX,targetY))
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while len(q) != 0:
        nowX, nowY = q.popleft()
        nowLen = length[nowX][nowY]
        for i in move:
            nextX = nowX + i[0]
            nextY = nowY + i[1]
            if nextX >= 0 and nextX < n and nextY >= 0 and nextY < m and mapDict[nextX][nextY] == '1' and length[nextX][nextY] == 0:
                length[nextX][nextY] = nowLen + 1
                q.append((nextX,nextY))
                
    for i in range(n):
        for j in range(m):
            if length[i][j] == 0 and mapDict[i][j] == '1':
                length[i][j] = -1
                
    for i in range(n):
        print(*length[i],sep=' ')
    return

if __name__ == '__main__':
    main()