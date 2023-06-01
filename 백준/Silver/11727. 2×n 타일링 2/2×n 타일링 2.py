import sys
input = sys.stdin.readline

def answer():
    n = int(input())
    if n == 1:
        return print(1)
    
    square = [0] * (n+1)
    square[1] = 1
    square[2] = 3
    for i in range(3,n+1):
        square[i] = (square[i-1] + ((square[i-2] * 2) % 10007)) % 10007
    return print(square[n])

if __name__ == "__main__":
    answer()