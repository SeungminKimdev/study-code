import sys
input = sys.stdin.readline

class Sudoku:
    def __init__(self, board):
        self.board = board
        self.row = [0] * 9
        self.col = [0] * 9
        self.box = [0] * 9
        self.empty_cells = []
        self.init_state()

    def init_state(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    self.empty_cells.append((i, j))
                else:
                    num = self.board[i][j]
                    self.set_bit(i, j, num, True)

    def set_bit(self, x, y, num, state):
        mask = 1 << (num - 1)
        self.row[x] = self.row[x] | mask if state else self.row[x] & ~mask
        self.col[y] = self.col[y] | mask if state else self.col[y] & ~mask
        box_index = (x // 3) * 3 + (y // 3)
        self.box[box_index] = self.box[box_index] | mask if state else self.box[box_index] & ~mask

    def is_valid(self, x, y, num):
        mask = 1 << (num - 1)
        box_index = (x // 3) * 3 + (y // 3)
        return not (self.row[x] & mask or self.col[y] & mask or self.box[box_index] & mask)

    def solve(self, index=0):
        if index == len(self.empty_cells):
            return True

        x, y = self.empty_cells[index]
        for num in range(1, 10):
            if self.is_valid(x, y, num):
                self.board[x][y] = num
                self.set_bit(x, y, num, True)

                if self.solve(index + 1):
                    return True

                self.board[x][y] = 0
                self.set_bit(x, y, num, False)
        return False

    def print_board(self):
        for row in self.board:
            print("".join(map(str, row)))


def main():
    board = [list(map(int, list(input().strip()))) for _ in range(9)]
    sudoku = Sudoku(board)
    sudoku.solve()
    sudoku.print_board()


if __name__ == "__main__":
    main()