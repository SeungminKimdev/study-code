import sys
input = sys.stdin.readline
from collections import deque

class Mapc:
    def __init__(self,N,M):
        self.array = {}
        self.n = N
        self.m = M
        self.visited = [[[0,0] for _ in range(M)] for _ in range(N)]
    
    def makeMap(self):
        for i in range(self.n):
            self.array[i] = input().rstrip()
            
    def bfs(self):
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        q = deque()
        q.append((0,0,0))
        self.visited[0][0][0] = 1
        
        while q:
            nowX,nowY,change = q.popleft()
            nowDis = self.visited[nowX][nowY][change]
            if nowX == self.n - 1 and nowY == self.m - 1:
                return nowDis
            
            for i in range(4):
                nextX = nowX + dx[i]
                nextY = nowY + dy[i]
                if nextX >= 0 and nextX < self.n and nextY >= 0 and nextY < self.m:
                    if self.array[nextX][nextY] == '0' and self.visited[nextX][nextY][change] == 0:
                        self.visited[nextX][nextY][change] = nowDis + 1
                        q.append((nextX,nextY,change))
                    elif self.array[nextX][nextY] == '1' and change == 0:
                        self.visited[nextX][nextY][1] = nowDis + 1
                        q.append((nextX,nextY,1))
        return -1

def solution():
    n, m = map(int,input().split())
    if n == 1 and m == 1:
        input()
        print('1')
        return
    mapc = Mapc(n,m)
    mapc.makeMap()
    print(mapc.bfs())
    
if __name__ == '__main__':
    solution()