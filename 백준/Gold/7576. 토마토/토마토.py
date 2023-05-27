import sys
input = sys.stdin.readline
from collections import deque
def tomatoDay(m, n, tomato):
    q = deque()
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == '1':
                q.append((i,j))
                
    if len(q) == 0:
        return print('-1')
    
    day = -1
    moveM = [0,0,1,-1]
    moveN = [1,-1,0,0]
    while q:
        newQ = deque()
        while q:
            nowN, nowM = q.pop()
            for i in range(4):
                tempM = nowM + moveM[i]
                tempN = nowN + moveN[i]
                if tempM < 0 or tempM >= m or tempN < 0 or tempN >= n:
                    continue
                if tomato[tempN][tempM] == '0':
                    tomato[tempN][tempM] = '1'
                    newQ.append((tempN,tempM))
        day += 1
        q = newQ

    for i in range(n):
        for j in tomato[i]:
            if j == '0':
                return print('-1')

    return print(day)

def main():
    m, n = map(int,input().split())
    tomato = {i:input().split() for i in range(n)}
    tomatoDay(m,n,tomato)
    
if __name__ == "__main__":
    main()