import sys
input = sys.stdin.readline

N,r,c = map(int,input().split())
global answer
answer = 0
def makeZ(x,y,size):
    global answer
    if x == r and y == c:
        print(answer)
        return 
    
    if r < x + size and r >= x and c < y + size and c >= y:
        halfN = size//2
        makeZ(x,y,halfN)
        makeZ(x,y+halfN,halfN)
        makeZ(x+halfN,y,halfN)
        makeZ(x+halfN,y+halfN,halfN)
    else:
        answer += size*size
        
makeZ(0,0,2**N)