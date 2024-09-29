n = int(input())

costs = [list(map(int, input().split())) for _ in range(n)]

answer = 1001 * n

for first in range(3): # R,G,B
    dp = [[0] * 3 for _ in range(n)]
    dp[0] = costs[0]
    for check in range(3):
        if check == first:
            dp[1][check] = 2002
        else:
            dp[1][check] = costs[0][first] + costs[1][check]

    for i in range(2, n):
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
        
    dp[n-1][first] = 1001 * n
    
    answer = min(answer, min(dp[n-1]))

print(answer)