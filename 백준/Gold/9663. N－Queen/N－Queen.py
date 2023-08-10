import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    board = [0] * n
    useNum = [False] * n
    global ans
    ans = 0
    def check(x):
        for i in range(x):
            if abs(board[x]-board[i]) == abs(x-i):
                return False
        return True
    
    def dfs(col):
        global ans
        if col == n:
            ans += 1
            return
        for i in range(n):
            if not useNum[i]:
                board[col] = i
                useNum[i] = True
                if check(col):
                    dfs(col+1)
                useNum[i] = False
    dfs(0)
    print(ans)

if __name__ == '__main__':
    solution()