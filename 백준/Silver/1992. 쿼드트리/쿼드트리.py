import sys
input = sys.stdin.readline

global ans
ans = ""
def check(n, startx, starty, video):
    fir = video[startx][starty]
    for i in range(startx, startx+n):
        for j in range(starty, starty+n):
            if video[i][j] != fir:
                return False
    return True

def quadTree(n, video, startx, starty):
    global ans
    if check(n,startx,starty,video):
        ans += video[startx][starty]
        return
    
    ans += "("
    divNum = n // 2
    quadTree(divNum, video, startx, starty)
    quadTree(divNum, video, startx, starty+divNum)
    quadTree(divNum, video, startx+divNum, starty)
    quadTree(divNum, video, startx+divNum, starty+divNum)
    ans += ")"

def main():
    n = int(input())
    video = []
    for _ in range(n):
        video += input().split()
    quadTree(n,video,0,0)
    print(ans)
    
if __name__ == "__main__":
    main()