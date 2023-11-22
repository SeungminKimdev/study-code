import sys
input = sys.stdin.readline

n,m = map(int,input().split())
shark = [list(map(int,input().split())) for _ in range(n)]
q = []
for i in range(n):
    for j in range(m):
        if shark[i][j] == 1:
            q.append((i,j))

moveX = [1,1,1,-1,-1,-1,0,0]
moveY = [0,1,-1,0,1,-1,1,-1]
ans = 0
while q:
    nowX, nowY = q.pop(0)
    for i in range(8):
        nextX = nowX + moveX[i]
        nextY = nowY + moveY[i]
        if nextX >= 0 and nextX < n and nextY >= 0 and nextY < m:
            if shark[nextX][nextY] == 0:
                ans = shark[nowX][nowY] + 1
                shark[nextX][nextY] = ans
                q.append((nextX,nextY))
print(ans-1)