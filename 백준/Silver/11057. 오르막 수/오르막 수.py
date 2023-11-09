import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    dp = {i:[0]*10 for i in range(2,n+1)}
    dp[1] = [1] * 10
    for i in range(2,n+1):
        for j in range(10):
            for k in range(j,10):
                dp[i][k] += dp[i-1][j]
                dp[i][k] %= 10007
    print(sum(dp[n]) % 10007)