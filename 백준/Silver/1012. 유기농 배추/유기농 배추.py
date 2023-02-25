#백준 1012
import sys
input = sys.stdin.readline

class baechu:
    
    def __init__(self, m, n, t):
        self.x = m
        self.y = n
        self.baechuMap = []
        self.visited = []
        for _ in range(m):
            self.baechuMap.append([0 for _ in range(n)])
            self.visited.append([0 for _ in range(n)])
        for _ in range(t):
            a, b = map(int,input().split())
            self.baechuMap[a][b] = 1
        
    def bfs(self, locX, locY):
        myQueue = [(locX,locY)]
        self.visited[locX][locY] = 1
        moveX = [1,-1,0,0]
        moveY = [0,0,1,-1]
        
        while len(myQueue) != 0:
            tempX, tempY = myQueue.pop(0)
            for i in range(4):
                nextX = tempX + moveX[i]
                nextY = tempY + moveY[i]
                if nextX >= 0 and nextX < self.x and nextY >= 0 and nextY < self.y and self.baechuMap[nextX][nextY] == 1 and self.visited[nextX][nextY] == 0:
                    self.visited[nextX][nextY] = 1
                    myQueue.append((nextX,nextY))
    
    def answer(self):
        answerNum = 0
        for i in range(self.x):
            for j in range(self.y):
                if self.baechuMap[i][j] == 1 and self.visited[i][j] == 0:
                    self.bfs(i,j)
                    answerNum += 1
        print(answerNum)

N = int(input())
for _ in range(N):
    m, n, t = map(int, input().split())
    mainBaechu = baechu(m,n,t)
    mainBaechu.answer()
    del mainBaechu