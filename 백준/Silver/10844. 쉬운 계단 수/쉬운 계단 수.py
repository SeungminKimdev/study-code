import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    stair = [[1 for _ in range(10)] for _ in range(n)]
    for i in range(1,n):
        stair[i][0] = stair[i-1][1]
        stair[i][9] = stair[i-1][8]
        for j in range(1,9):
            stair[i][j] = (stair[i-1][j-1] + stair[i-1][j+1]) % 1000000000
    print(sum(stair[n-1][1:]) % 1000000000)