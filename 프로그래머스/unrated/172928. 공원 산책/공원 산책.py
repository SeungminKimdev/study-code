def solution(park, routes):
    X = 0
    Y = 0
    maxSizeX = len(park)
    maxSizeY = len(park[0])
    for i in range(maxSizeX):
        for j in range(maxSizeY):
            if park[i][j] == "S":
                X = i
                Y = j
                break
        
    moving = {'N' : [-1,0],
        'S' : [1,0],
        'W' : [0,-1],
        'E' : [0,1]}
    
    def move(route, num, x, y):
        returnx = x
        returny = y
        for _ in range(num):
            dx = returnx + route[0]
            dy = returny + route[1]
            if dx >= 0 and dx < maxSizeX and dy >= 0 and dy < maxSizeY:
                if park[dx][dy] != 'X':
                    returnx = dx
                    returny = dy
                else:
                    returnx = x
                    returny = y
                    break
            else:
                returnx = x
                returny = y
                break
        return returnx, returny
    
    for i in routes:
        command,num = i.split()
        num = int(num)
        X,Y = move(moving[command],num,X,Y)
    return [X,Y]