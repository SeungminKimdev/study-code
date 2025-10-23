import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    fuel = [list(map(int, input().split())) for _ in range(N)]
    q = [(fuel[0][i], -2, i) for i in range(M)]
    
    for i in range(1, N):
        q_len = len(q)
        for _ in range(q_len):
            fuel_sum, before_loot, line = q.pop(0)
            for loot in [-1, 0, 1]:
                if before_loot == loot:
                    continue
                next_line = line + loot
                if 0 <= next_line < M:
                    q.append((fuel_sum + fuel[i][next_line], loot, next_line))
    
    print(min(q)[0])
    return

if __name__ == "__main__":
    main()