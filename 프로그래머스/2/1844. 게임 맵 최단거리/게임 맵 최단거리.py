def solution(maps):
    m = len(maps[0])
    n = len(maps)
    q = [(0,0)]
    while q:
        nowX, nowY = q.pop(0)
        nowDis = maps[nowX][nowY]
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for i in range(4):
            nextX = nowX + dx[i]
            nextY = nowY + dy[i]
            if nextX >= 0 and nextX < n and nextY >= 0 and nextY < m:
                if maps[nextX][nextY] == 1:
                    q.append((nextX,nextY))
                    maps[nextX][nextY] += nowDis

    if maps[-1][-1] == 1:
        answer = -1
    else:
        answer = maps[-1][-1]
    return answer