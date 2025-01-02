import sys
input = sys.stdin.readline

def move(color, dx, dy, board):
    x, y = color
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
    return [x, y]

def main():
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        tempLine = list(input().strip())
        for j in range(m):
            if tempLine[j] == 'R':
                red = [i, j]
            elif tempLine[j] == 'B':
                blue = [i, j]
        board.append(tempLine)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = [(red, blue, 0)]
    while q:
        r, b, turn = q.pop(0)
        if turn >= 10:
            print(-1)
            return
        
        for i in range(4):
            nextR = move(r, dx[i], dy[i], board)
            nextB = move(b, dx[i], dy[i], board)
            if board[nextB[0]][nextB[1]] == 'O':
                continue
            if board[nextR[0]][nextR[1]] == 'O':
                print(turn+1)
                return
            if nextR == nextB:
                if i == 0:
                    if r[0] > b[0]:
                        nextR[0] += 1
                    else:
                        nextB[0] += 1
                elif i == 1:
                    if r[0] > b[0]:
                        nextB[0] -= 1
                    else:
                        nextR[0] -= 1
                elif i == 2:
                    if r[1] > b[1]:
                        nextR[1] += 1
                    else:
                        nextB[1] += 1
                else:
                    if r[1] > b[1]:
                        nextB[1] -= 1
                    else:
                        nextR[1] -= 1
            if r != nextR or b != nextB:
                q.append((nextR, nextB, turn+1))
    print(-1)

if __name__ == "__main__":
	main()