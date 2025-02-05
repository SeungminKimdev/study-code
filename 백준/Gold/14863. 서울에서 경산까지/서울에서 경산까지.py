import sys
input = sys.stdin.readline

def main():
    n, costs = map(int, input().split())
    arrays = [list(map(int, input().split())) for _ in range(n)]
    dp = [[] for _ in range(n+1)] # 모금액 합, 비용합
    dp[0].append((0,0))
    
    for i in range(1, n+1):
        for money, cost in dp[i-1]:
            nextCost = cost + arrays[i-1][0]
            if nextCost < costs or (nextCost == costs and i == n):
                dp[i].append((money+arrays[i-1][1], nextCost))
            nextCost = cost + arrays[i-1][2]
            if nextCost < costs or (nextCost == costs and i == n):
                dp[i].append((money+arrays[i-1][3], nextCost))
    
    print(max(dp[n])[0])


if __name__ == "__main__":
    main()