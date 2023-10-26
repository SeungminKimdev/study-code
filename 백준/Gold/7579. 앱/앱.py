import sys
input = sys.stdin.readline

def knapsack(n,m,memory,cost):
    dp = [0] * 10001
    for i in range(n):
        for j in range(10000,-1,-1):
            if cost[i] <= j:
                dp[j] = max(dp[j],dp[j-cost[i]]+memory[i])
    costN = 0
    while(dp[costN] < m):
        costN += 1
    return print(costN)

if __name__ == '__main__':
    n,m = map(int,input().split())
    memory = list(map(int,input().split()))
    cost = list(map(int,input().split()))
    knapsack(n,m,memory,cost)