import sys
sys.setrecursionlimit(100000)

def quadtree(arr,x,y,size,ans):
    check = arr[x][y]
    if size == 1:
        ans[check] += 1
        return
    for i in range(x,x+size):
        for j in range(y,y+size):
            if arr[i][j] != check:
                halfSize = size//2
                quadtree(arr,x,y,halfSize,ans)
                quadtree(arr,x+halfSize,y,halfSize,ans)
                quadtree(arr,x,y+halfSize,halfSize,ans)
                quadtree(arr,x+halfSize,y+halfSize,halfSize,ans)
                return
    ans[check] += 1

def solution(arr):
    size = len(arr)
    answer = [0,0]
    quadtree(arr,0,0,size,answer)
    return answer