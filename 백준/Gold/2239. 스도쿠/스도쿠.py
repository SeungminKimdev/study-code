import sys
input = sys.stdin.readline

class Sudoku:
    def __init__(self):
        self.board = [list(map(int, list(input().strip()))) for _ in range(9)]
    
    def possibleNumber(self, x, y, num):
        for i in range(9):
            if self.board[x][i] == num or self.board[i][y] == num:
                return False
        x //= 3
        y //= 3
        for i in range(x * 3, (x + 1) * 3):
            for j in range(y * 3, (y + 1) * 3):
                if self.board[i][j] == num:
                    return False
        return True
    
    def backtracking(self):
        empty_cells = [(i, j) for i in range(9) for j in range(9) if self.board[i][j] == 0]

        index = 0
        while index < len(empty_cells):
            x, y = empty_cells[index]
            found = False

            for num in range(self.board[x][y] + 1, 10):
                if self.possibleNumber(x, y, num):
                    self.board[x][y] = num
                    index += 1
                    found = True
                    break
            
            if not found:
                self.board[x][y] = 0
                index -= 1
    
    def printBoard(self):
        for i in range(9):
            print(*self.board[i],sep='')

def main():
    sudoku = Sudoku()
    sudoku.backtracking()
    sudoku.printBoard()

if __name__ == "__main__":
	main()