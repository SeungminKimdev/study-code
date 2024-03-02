def solution(land):
    length = len(land)
    width = len(land[0])
    blockLand = [[0]*length for _ in range(width)]
    visited = [[False]*width for _ in range(length)]
    blockNum = 1
    fuel = [0]
    
    for i in range(length):
        for j in range(width):
            if land[i][j] == 1 and not visited[i][j]:
                q = [(i,j)]
                blockLand[j][i] = blockNum
                visited[i][j] = True
                dx = [1,-1,0,0]
                dy = [0,0,1,-1]
                tempFuel = 1
                while q:
                    nowX, nowY = q.pop(0)
                    for k in range(4):
                        nextX = nowX + dx[k]
                        nextY = nowY + dy[k]
                        if nextX >= 0 and nextX < length and nextY >= 0 and nextY < width and not visited[nextX][nextY] and land[nextX][nextY] == 1:
                            q.append((nextX,nextY))
                            visited[nextX][nextY] = True
                            blockLand[nextY][nextX] = blockNum
                            tempFuel += 1
                fuel.append(tempFuel)
                blockNum += 1
    
    answer = 0
    for i in range(width):
        temp = set(blockLand[i])
        tempSum = 0
        for j in temp:
            tempSum += fuel[j]
        answer = max(answer,tempSum)
    return answer