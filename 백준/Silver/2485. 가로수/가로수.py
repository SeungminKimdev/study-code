import sys
input = sys.stdin.readline
import math

def main():
    N = int(input())
    a = int(input())
    arr = []
    for _ in range(N-1):
        num = int(input())
        arr.append(num - a)
        a = num

    g = arr[0]
    for j in range(1, len(arr)):
        g = math.gcd(g, arr[j])

    result = 0
    for each in arr:
        result += each // g - 1
    print(result)

if __name__ == "__main__":
    main()