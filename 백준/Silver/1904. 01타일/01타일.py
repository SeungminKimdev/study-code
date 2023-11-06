import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    dp = [0,1,2]
    if n < 3:
        print(dp[n])
    else:
        for i in range(2,n):
            dp.append((dp[i]+dp[i-1])%15746)
        print(dp[-1])