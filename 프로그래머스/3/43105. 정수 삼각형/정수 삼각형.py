def solution(triangle):
    tg = triangle
    depth = len(tg)
    for i in range(1,depth):
        length = len(tg[i])
        tg[i][0] += tg[i-1][0]
        for j in range(1,length-1):
            tg[i][j] += max(tg[i-1][j-1],tg[i-1][j])
        tg[i][-1] += tg[i-1][-1]
    answer = max(tg[-1])
    return answer