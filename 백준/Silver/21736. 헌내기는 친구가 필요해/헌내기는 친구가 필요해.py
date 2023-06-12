import sys
input = sys.stdin.readline
from collections import deque

def main():
    n, m = map(int,input().split())
    campus = {}
    visited = {}
    startX = startY = 0
    for i in range(n):
        inputS = input().rstrip()
        for j in range(m):
            if inputS[j] == 'I':
                startX = i
                startY = j
        campus[i] = inputS
        visited[i] = [False] * m
        
    meet = 0
    visited[startX][startY] = True
    moveX = [0,0,1,-1]
    moveY = [1,-1,0,0]
    q = deque()
    q.append((startX,startY))
    while q:
        nowX, nowY = q.popleft()
        
        for i in range(4):
            nextX = nowX + moveX[i]
            nextY = nowY + moveY[i]
            if nextX >= 0 and nextX < n and nextY >= 0 and nextY < m and not visited[nextX][nextY]:
                if campus[nextX][nextY] != 'X':
                    if campus[nextX][nextY] == 'P':
                        meet += 1
                    visited[nextX][nextY] = True
                    q.append((nextX,nextY))
    if meet == 0:
        print('TT')
    else:
        print(meet)

if __name__ == "__main__":
    main()