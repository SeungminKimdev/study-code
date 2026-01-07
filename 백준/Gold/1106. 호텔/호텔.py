import sys
from collections import deque
input = sys.stdin.readline

def main():
    target_customer, city_count = map(int, input().split())
    costs = []
    dp = [0] * 1001 # target = idx 0
    for _ in range(city_count):
        cost, add_customer = map(int, input().split())
        costs.append((cost, add_customer))
    q = deque([(target_customer, 0)])
    while q:
        target, cost = q.popleft()
        for c, a in costs:
            new_cost = cost + c
            new_target = max(0, target - a)
            if dp[new_target] == 0 or dp[new_target] > new_cost:
                dp[new_target] = new_cost
                q.append((new_target, new_cost))
    print(dp[0])
    return

if __name__ == "__main__":
    main()