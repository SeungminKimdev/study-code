import sys
input = sys.stdin.readline

def main():
    n = int(input())
    move = []
    for _ in range(6):
        loc, length = map(int,input().split())
        move.append((loc,length))
    move += move
    
    for i in range(3,12):
        if move[i][0] == move[i-2][0] and move[i-3][0] == move[i-1][0]:
            big = move[i+1][1] * move[i+2][1]
            small = move[i-1][1] * move[i-2][1]
            print(n*(big-small))
            break
    return

if __name__ == '__main__':
    main()