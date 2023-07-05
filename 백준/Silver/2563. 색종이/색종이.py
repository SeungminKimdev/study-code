import sys
input = sys.stdin.readline

def main():
    n = int(input())
    paper = [[0]*100 for _ in range(100)]
    numList = []
    for _ in range(n):
        numList.append(list(map(int,input().split())))
    ans = 0
    for num in numList:
        x, y = num
        for i in range(x,x+10):
            for j in range(y,y+10):
                if paper[i][j] == 0:
                    ans += 1
                paper[i][j] = 1
    print(ans)
    return

if __name__ == '__main__':
    main()