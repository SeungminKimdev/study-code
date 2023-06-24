import sys
input = sys.stdin.readline
import math
def main():
    n = int(input())
    for _ in range(n):
        M, N, x, y = map(int, input().split())
        maxNum = math.lcm(M,N)
        ans = -1
        for i in range(0,maxNum+1,M):
            check = i + x - y
            if check >= 0 and check % N == 0:
                ans = check + y
                break
        print(ans)
    return

if __name__ == '__main__':
    main()