import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    price = list(map(int,input().split()))
    dp = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(n):
            if i < j+1:
                break
            dp[i] = max(dp[i],dp[i-j-1]+price[j])
    print(dp[-1])