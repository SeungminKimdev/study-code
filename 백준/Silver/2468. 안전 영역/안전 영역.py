import sys
import copy
input = sys.stdin.readline

def bfs(land, i, j, n, h):
    q = [(i, j)]
    while q:
        x, y = q.pop(0)
        land[x][y] = -1
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and land[nx][ny] > h:
                q.append((nx, ny))
                land[nx][ny] = -1

def main():
    n = int(input())
    land = []
    maxLand = 0
    answer = 0
    for _ in range(n):
        inputList = list(map(int, input().split()))
        maxLand = max(maxLand, max(inputList))
        land.append(inputList)
    
    for h in range(0, maxLand):
        tempAnswer = 0
        tempLand = copy.deepcopy(land)
        for i in range(n):
            for j in range(n):
                if tempLand[i][j] > h:
                    bfs(tempLand, i, j, n, h)
                    tempAnswer += 1
        answer = max(answer, tempAnswer)
    print(answer)

if __name__ == "__main__":
    main()
