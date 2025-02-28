import sys
input = sys.stdin.readline

def main():
    test_case = int(input())
    for _ in range(test_case):
        m, n = map(int, input().split())
        grid = [list(input().split()) for _ in range(m)]
        move_count = 0 # 총 이동 횟수
        for i in range(n):
            final_block_loc =  m - 1 # 현재 블럭의 최종 위치
            for j in range(m-1, -1, -1):
                if grid[j][i] == '1':
                    move_count += abs(final_block_loc - j)
                    final_block_loc -= 1
        print(move_count)
if __name__ == "__main__":
    main()