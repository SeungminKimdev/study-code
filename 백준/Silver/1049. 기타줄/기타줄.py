import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    six = 1000
    one = 1000
    for _ in range(m):
        a, b = map(int, input().split())
        six = min(six, a)
        one = min(one, b)
    if six < one * 6:
        answer = n // 6 * six + min(six, (n % 6) * one)
    else: 
        answer = one * n
    print(answer)

if __name__ == "__main__":
    main()