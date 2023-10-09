import sys
input = sys.stdin.readline

n, m = map(int,input().split())
board = [input() for _ in range(n)]
visited = [False for _ in range(26)]
global ans
ans = 0

def dfs(x,y,visited,depth):
    global ans
    ans = max(ans,depth)
    visited[ord(board[x][y])-65] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if nextX>=0 and nextX < n and nextY >= 0 and nextY < m:
            if not visited[(ord(board[nextX][nextY]))-65]:
                dfs(nextX,nextY,visited,depth+1)
                visited[ord(board[nextX][nextY])-65] = False

dfs(0,0,visited,1)
print(ans)
