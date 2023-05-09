import sys
input = sys.stdin.readline
score = [0,0,0]
def checkSame(x,y,size,paper) -> bool:
    checkNum = paper[x][y]
    for i in range(size):
        for j in range(size):
            if checkNum != paper[x+i][y+j]:
                return False
    return True

def dividePaper(x,y,size,paper) -> None:
    if checkSame(x,y,size,paper):
        score[int(paper[x][y])+1] += 1
        return
    else:
        cutSize = size // 3
        for i in range(3):
            for j in range(3):
                dividePaper(x+cutSize*i,y+cutSize*j,cutSize,paper)
    return

n = int(input())
paper = [input().split() for _ in range(n)]

dividePaper(0,0,n,paper)
print(*score,sep='\n')