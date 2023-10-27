import sys
input = sys.stdin.readline
import math

def main():
    n = int(input())
    for _ in range(n):
        a, b = map(int,input().split())
        print(math.lcm(a,b))

if __name__ == "__main__":
    main()