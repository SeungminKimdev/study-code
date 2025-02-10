import sys
input = sys.stdin.readline

class Sudoku:
    def __init__(self):
        self.board = [list(input().rstrip()) for _ in range(9)]
        self.complete_sdoku = False

    def check_board(self):
        for i in range(9):
            row_check = set()
            col_check = set()
            for j in range(9):
                if self.board[i][j] != '0':
                    if self.board[i][j] in row_check:
                        return False
                    row_check.add(self.board[i][j])
                if self.board[j][i] != '0':
                    if self.board[j][i] in col_check:
                        return False
                    col_check.add(self.board[j][i])
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block_check = set()
                for k in range(3):
                    for l in range(3):
                        if self.board[i+k][j+l] != '0':
                            if self.board[i+k][j+l] in block_check:
                                return False
                            block_check.add(self.board[i+k][j+l])
        
        return True
    
    def possible_number(self, x, y):
        possible = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(9):
            if self.board[x][i] in possible:
                possible.remove(self.board[x][i])
            if self.board[i][y] in possible:
                possible.remove(self.board[i][y])
        bx = (x // 3) * 3
        by = (y // 3) * 3
        for i in range(bx, bx + 3):
            for j in range(by, by + 3):
                if self.board[i][j] in possible:
                    possible.remove(self.board[i][j])
        return possible

    def fill_sdoku(self):
        if self.complete_sdoku:
            return

        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '0':
                    poss = self.possible_number(i, j)
                    for num in poss:
                        self.board[i][j] = num
                        self.fill_sdoku()
                        if self.complete_sdoku:
                            return
                        self.board[i][j] = '0'
                    return
        self.print_board()
        self.complete_sdoku = True

    def print_board(self):
        for row in self.board:
            print(''.join(row))

    def check_sdoku(self):
        if not self.complete_sdoku:
            print("Could not complete this grid.")

def main():
    t = int(input().strip())
    for tc in range(t):
        sudoku = Sudoku()
        if sudoku.check_board():
            sudoku.fill_sdoku()
            sudoku.check_sdoku()
        else:
            print("Could not complete this grid.")
        
        if tc != t - 1:
            print()

if __name__ == "__main__":
    main()
