def cross_point(line1, line2):
    if line1[0] * line2[1] - line1[1] * line2[0] == 0:
        return (False,0,0)
    x = (line1[1]*line2[2] - line1[2]*line2[1]) / (line1[0]*line2[1] - line1[1]*line2[0])
    y = (line1[2]*line2[0] - line1[0]*line2[2]) / (line1[0]*line2[1] - line1[1]*line2[0])
    return (True,x,y)

def solution(line):
    length = len(line)
    ansPoint = []
    for i in range(length):
        for j in range(i,length):
            check, x, y = cross_point(line[i],line[j])
            if check and int(x) == x and int(y) == y:
                ansPoint.append((int(x),int(y)))
    startX = min(ansPoint, key = lambda x:x[0])[0]
    startY = min(ansPoint, key = lambda x:x[1])[1]
    endX = max(ansPoint, key = lambda x:x[0])[0]
    endY = max(ansPoint, key = lambda x:x[1])[1]
    answer = [["."]*(endX-startX+1) for _ in range(endY-startY+1)]
    for i,j in ansPoint:
        answer[j-startY][i-startX] = "*"
    ans = []
    for i in range(endY-startY+1):
        ans.append("".join(answer[i]))
    return ans[::-1]