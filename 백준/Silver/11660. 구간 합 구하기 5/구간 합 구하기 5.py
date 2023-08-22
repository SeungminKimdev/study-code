import sys
input = sys.stdin.readline

def solution():
    n,m = map(int,input().split())
    arr = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        inputArr = list(map(int,input().split()))
        for j in range(1,n+1):
            arr[i][j]= arr[i][j-1] + arr[i-1][j]-arr[i-1][j-1]+inputArr[j-1]
    
    for _ in range(m):
        x1, y1, x2, y2 = map(int,input().split())
        ans = arr[x2][y2] - arr[x2][y1-1] - arr[x1-1][y2] + arr[x1-1][y1-1]
        print(ans)
        
if __name__ == '__main__':
    solution()