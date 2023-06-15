import sys
input = sys.stdin.readline

def main():
    score = {}
    for i in range(9):
        score[i] = list(map(int,input().split()))
    x = y = 0
    maxNum = score[0][0]
    for i in range(9):
        for j in range(9):
            if score[i][j] > maxNum:
                x = i
                y = j
                maxNum = score[i][j]
    print(maxNum)
    print(str(x+1) + " " + str(y+1))

if __name__ == "__main__":
    main()