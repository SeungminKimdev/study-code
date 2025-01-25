import sys
input = sys.stdin.readline

def basic(x, y, arr):
    arr[x][y] = "*"
    arr[x+1][y-1] = "*"
    arr[x+1][y+1] = "*"
    for i in range(5):
        arr[x+2][y-2+i] = "*"

def star(x, y, length, arr):
    if length == 3:
        basic(x, y, arr)
        return
    star(x, y, length//2, arr)
    star(x+length//2, y-length//2, length//2, arr)
    star(x+length//2, y+length//2, length//2, arr)

def main():
    n = int(input())
    arr = [[" " for _ in range(2*n-1)] for _ in range(n)]
    star(0, n-1, n, arr)
    for i in range(n):
        print("".join(arr[i]))

if __name__ == "__main__":
    main()