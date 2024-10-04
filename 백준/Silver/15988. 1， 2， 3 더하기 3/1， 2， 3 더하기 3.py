import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dp = [0, 1, 2, 4]
    for _ in range(n):
        target = int(input())
        dp_len = len(dp) - 1
        if dp_len < target:
            for i in range(dp_len, target):
                dp.append((dp[i] + dp[i-1] + dp[i-2]) % 1000000009)
        print(dp[target])
    return

if __name__ == "__main__":
    main()