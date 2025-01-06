import sys
input = sys.stdin.readline

def main():
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    body = [0] * 5 # 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리
    
    findHead = False
    for i in range(n):
        if findHead:
            break
        for j in range(n):
            if board[i][j] == '*':
                head = (i, j) # heart = i+1, j
                findHead = True
                break
    
    for i in range(n): # 왼쪽 팔
        if board[head[0] + 1][i] == '*':
            body[0] = head[1] - i
            break
    
    for i in range(n-1, 0, -1): # 오른쪽 팔
        if board[head[0] + 1][i] == '*':
            body[1] = i - head[1]
            break
    
    for i in range(head[0] + 2, n): # 허리
        if board[i][head[1]] == '*':
            body[2] += 1
        else:
            midLeg = (i, head[1]) # 다리 중앙
            break
    
    for i in range(midLeg[0], n): # 다리
        if board[i][head[1] - 1] != '*' and board[i][head[1] + 1] != '*':
            break
        if board[i][head[1] - 1] == '*': # 왼쪽 다리
            body[3] += 1
        if board[i][head[1] + 1] == '*': # 오른쪽 다리
            body[4] += 1
    
    print(f'{head[0] + 2} {head[1] + 1}')
    print(*body)

if __name__ == "__main__":
	main()