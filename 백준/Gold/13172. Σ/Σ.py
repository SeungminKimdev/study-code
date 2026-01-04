import sys
input = sys.stdin.readline

MOD = 1000000007

def main():
    n = int(input().strip())
    total_expectation = 0
    
    for _ in range(n):
        N, S = map(int, input().strip().split())
        
        if S % N == 0: # 나누어 떨어지는 경우
            print(S // N)
            continue
        
        current_expectation = (S * pow(N, MOD - 2, MOD)) % MOD
        total_expectation = (total_expectation + current_expectation) % MOD
    
    print(total_expectation)
    return

if __name__ == "__main__":
    main()