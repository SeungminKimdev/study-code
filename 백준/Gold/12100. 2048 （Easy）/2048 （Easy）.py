import sys
input = sys.stdin.readline

def find_maximum_block(size, board, depth):
    if depth == 0:
        return max(max(row) for row in board)
    
    max_block = 0
    for way in ['u', 'd', 'l', 'r']:
        new_board = move(size, board, way)
        max_block = max(max_block, find_maximum_block(size, new_board, depth - 1))
    
    return max_block

def move(size, board, way):
    new_board = [[0] * size for _ in range(size)]
    if way == 'u': # up
        for i in range(size):
            now_block = 0 # setting block index
            for j in range(size):
                if board[j][i] == 0:
                    continue
                if new_board[now_block][i] == 0:
                    new_board[now_block][i] = board[j][i]
                elif new_board[now_block][i] == board[j][i]:
                    new_board[now_block][i] *= 2
                    now_block += 1
                else:
                    now_block += 1
                    new_board[now_block][i] = board[j][i]
    elif way == 'd': # down
        for i in range(size):
            now_block = size-1 # setting block index
            for j in range(size-1, -1, -1):
                if board[j][i] == 0:
                    continue
                if new_board[now_block][i] == 0:
                    new_board[now_block][i] = board[j][i]
                elif new_board[now_block][i] == board[j][i]:
                    new_board[now_block][i] *= 2
                    now_block -= 1
                else:
                    now_block -= 1
                    new_board[now_block][i] = board[j][i]
    elif way == 'l': # left
        for i in range(size):
            now_block = 0 # setting block index
            for j in range(size):
                if board[i][j] == 0:
                    continue
                if new_board[i][now_block] == 0:
                    new_board[i][now_block] = board[i][j]
                elif new_board[i][now_block] == board[i][j]:
                    new_board[i][now_block] *= 2
                    now_block += 1
                else:
                    now_block += 1
                    new_board[i][now_block] = board[i][j]
    elif way == 'r': # right
        for i in range(size):
            now_block = size-1 # setting block index
            for j in range(size-1, -1, -1):
                if board[i][j] == 0:
                    continue
                if new_board[i][now_block] == 0:
                    new_board[i][now_block] = board[i][j]
                elif new_board[i][now_block] == board[i][j]:
                    new_board[i][now_block] *= 2
                    now_block -= 1
                else:
                    now_block -= 1
                    new_board[i][now_block] = board[i][j]
    else:
        raise ValueError("Invalid move direction")
    return new_board

def main():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = find_maximum_block(N, board, 5)
    print(result)

if __name__ == "__main__":
    main()