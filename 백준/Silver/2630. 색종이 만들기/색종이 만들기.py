import sys
input = sys.stdin.readline

paperAns = [0,0]
def checkBox(paper, startx, starty, n):
    if n == 1:
        paperAns[paper[startx][starty]] += 1
        return
    check = True
    fir = paper[startx][starty]
    for i in range(startx,startx+n):
        for j in range(starty,starty+n):
            if paper[i][j] != fir:
                check = False
                temp = n // 2
                checkBox(paper,startx,starty,temp)
                checkBox(paper,startx,starty+temp,temp)
                checkBox(paper,startx+temp,starty,temp)
                checkBox(paper,startx+temp,starty+temp,temp)
                return
    if check:
        paperAns[fir] += 1
    return

n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int,input().split())))
checkBox(paper,0,0,n)
print(*paperAns, sep="\n")