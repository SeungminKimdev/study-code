import sys
input = sys.stdin.readline

def knapsack_dp(capacity, n, size, value):
    memo = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if size[i-1] > j:
                memo[i][j] = memo[i-1][j]
            else:
                memo[i][j] = max(value[i-1] + memo[i-1][j-size[i-1]], memo[i-1][j])
    return memo[n][capacity]

N, K = map(int, sys.stdin.readline().split()) #N = 물품 수, K = 한계 무게
size = []
value = []
for _ in range(N):
    W, V = map(int, sys.stdin.readline().split()) #W = 무게, V = 가치
    size.append(W)
    value.append(V)
print(knapsack_dp(K, N, size, value))