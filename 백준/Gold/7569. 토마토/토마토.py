import sys
input = sys.stdin.readline
from collections import deque
def tomatoDay(m, n, h, tomato):
    q = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomato[i][j][k] == '1':
                    q.append((i,j,k))
                
    if len(q) == 0:
        return print('-1')
    
    day = -1
    moveM = [0,0,1,-1,0,0]
    moveN = [1,-1,0,0,0,0]
    moveH = [0,0,0,0,1,-1]
    while q:
        newQ = deque()
        while q:
            nowH, nowN, nowM = q.pop()
            for i in range(6):
                tempM = nowM + moveM[i]
                tempN = nowN + moveN[i]
                tempH = nowH + moveH[i]
                if tempM < 0 or tempM >= m or tempN < 0 or tempN >= n or tempH < 0 or tempH >= h:
                    continue
                if tomato[tempH][tempN][tempM] == '0':
                    tomato[tempH][tempN][tempM] = '1'
                    newQ.append((tempH,tempN,tempM))
        day += 1
        q = newQ

    for i in range(h):
        for j in range(n):
            for k in tomato[i][j]:
                if k == '0':
                    return print('-1')

    return print(day)

def main():
    m, n, h = map(int,input().split())
    tomato = {}
    for i in range(h):
        tomato[i] = {j:input().split() for j in range(n)}
    tomatoDay(m,n,h,tomato)
    
if __name__ == '__main__':
    main()