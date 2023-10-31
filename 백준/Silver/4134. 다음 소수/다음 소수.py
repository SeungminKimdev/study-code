import sys
input = sys.stdin.readline
import math

def main():
    n = int(input())
    for _ in range(n):
        num = int(input())
        if num < 3:
            print(2)
            continue
        while 1:
            check = True
            for i in range(2,int(math.sqrt(num))+1):
                if num % i == 0:
                    num += 1
                    check = False
                    break
            if check:
                break
        print(num)

if __name__ == "__main__":
    main()