import sys
input = sys.stdin.readline

def findRoad():
    n = int(input())
    road = {i:[] for i in range(n)}
    for i in range(n):
        road[i] += list(map(int, input().split()))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if road[i][j] == 0 and road[i][k] == 1 and road[k][j] == 1:
                    road[i][j] = 1
    for i in range(n):
        print(*road[i],sep=" ")
    return

if __name__ == "__main__":
    findRoad()