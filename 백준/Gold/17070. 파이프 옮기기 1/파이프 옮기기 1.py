import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    
    dp = [[[0] * 3 for _ in range(n)] for _ in range(n)] # x, y, 모양(가로,세로,대각선)
    dp[0][1][0] = 1

    for x in range(n):
        for y in range(1, n):
            if arr[x][y] == '1':
                continue
            
            if y - 1 >= 0: # 가로
                dp[x][y][0] += dp[x][y-1][0] + dp[x][y-1][2]
            if x - 1 >= 0: # 세로
                dp[x][y][1] += dp[x-1][y][1] + dp[x-1][y][2]
            if x - 1 >= 0 and y - 1 >= 0 and arr[x-1][y] == '0' and arr[x][y-1] == '0': # 대각선
                dp[x][y][2] += dp[x-1][y-1][0] + dp[x-1][y-1][1] + dp[x-1][y-1][2]
    
    print(sum(dp[n-1][n-1]))

if __name__ == "__main__":
	main()