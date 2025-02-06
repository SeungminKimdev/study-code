import sys
input = sys.stdin.readline

def main():
    n = int(input())
    answer = 8
    num = 1
    while True:
        if num > n:
            print(answer + 1)
            break
        elif num == n:
            print(answer + 2)
            break
        else:
            num *= 2
            answer += 1 

if __name__ == "__main__":
    main()