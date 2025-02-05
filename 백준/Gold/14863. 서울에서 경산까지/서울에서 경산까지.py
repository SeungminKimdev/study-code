import sys
input = sys.stdin.readline

def prune(state):
    items = sorted(state.items())
    pruned = {}
    best = -1
    for c, m in items:
        if m > best:
            pruned[c] = m
            best = m
    return pruned

def main():
    n, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    dp = {0: 0}
    for i in range(n):
        new_dp = {}
        for cost, money in dp.items():
            nc = cost + arr[i][0]
            if (i == n - 1 and nc <= C) or (i < n - 1 and nc < C):
                new_dp[nc] = max(new_dp.get(nc, 0), money + arr[i][1])
            nc = cost + arr[i][2]
            if (i == n - 1 and nc <= C) or (i < n - 1 and nc < C):
                new_dp[nc] = max(new_dp.get(nc, 0), money + arr[i][3])
        dp = prune(new_dp)
    print(max(dp.values()))

if __name__ == "__main__":
    main()
