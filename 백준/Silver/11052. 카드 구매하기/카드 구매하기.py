import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    price = list(map(int,input().split()))
    dp = [0] * (n+1)
    for i in range(1,n+1):
        for j in range(i):
            dp[i] = max(dp[i],dp[i-j-1]+price[j])
    print(dp[n])