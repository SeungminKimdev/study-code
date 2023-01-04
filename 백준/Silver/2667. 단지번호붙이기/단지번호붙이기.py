import sys

n = int(sys.stdin.readline())

map = []
visited = [[False for _ in range(n)] for _ in range(n)]
answer = []

for _ in range(n):
    a = str(sys.stdin.readline())
    map.append([a[i] for i in range(n)])

answerNum = 0

moveX = [1,-1,0,0]
moveY = [0,0,1,-1]

for i in range(n):
    for j in range(n):
        if ((not visited[i][j]) and map[i][j] == '1'):
            nowNum = 1
            queue = [[i,j]]
            while(len(queue) != 0):
                temp = queue.pop(0)
                X = temp[0]
                Y = temp[1]
                visited[X][Y] = True
                
                for k in range(4):
                    nextX = X + moveX[k]
                    nextY = Y + moveY[k]
                    if(nextX >= 0 and nextX < n and nextY >= 0 and nextY < n):
                        if ((not visited[nextX][nextY]) and map[nextX][nextY] == '1'):
                            queue.append([nextX,nextY])
                            visited[nextX][nextY] = True
                            nowNum += 1
            answerNum += 1
            answer.append(nowNum)
        else:
            visited[i][j] = True

answer.sort()
print(answerNum)
for i in answer:
    print(i)